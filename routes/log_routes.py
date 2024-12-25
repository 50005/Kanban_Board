from flask import Blueprint, request, jsonify, render_template
from sqlalchemy.orm import Session
from services.log_service import LogService
from database import get_db
from schemas.log import LogCreate, Log  # Убедитесь, что импорт правильный

log_blueprint = Blueprint('log', __name__)

@log_blueprint.route("/", methods=["POST"])
def create_log():
    log_data = LogCreate(**request.form)
    db: Session = next(get_db())
    log_service = LogService(db)
    created_log = log_service.create_log(
        message=log_data.message,
        timestamp=log_data.timestamp
    )
    return render_template("log/view.html", log=Log.from_orm(created_log)), 201

@log_blueprint.route("/create", methods=["GET"])
def create_log_form():
    return render_template("log/create.html")

@log_blueprint.route("/<int:log_id>", methods=["GET"])
def get_log_by_id(log_id: int):
    db: Session = next(get_db())
    log_service = LogService(db)
    log = log_service.get_log_by_id(log_id)
    if not log:
        return jsonify({"message": "Log not found"}), 404
    return render_template("log/view.html", log=Log.from_orm(log))

@log_blueprint.route("/", methods=["GET"])
def get_all_logs():
    db: Session = next(get_db())
    log_service = LogService(db)
    logs = log_service.get_all_logs()
    return render_template("log/view_all.html", logs=[Log.from_orm(log) for log in logs])

@log_blueprint.route("/<int:log_id>/edit", methods=["GET"])
def get_edit_log_form(log_id: int):
    db: Session = next(get_db())
    log_service = LogService(db)
    log = log_service.get_log_by_id(log_id)
    if not log:
        return jsonify({"message": "Log not found"}), 404
    return render_template("log/edit.html", log=Log.from_orm(log))

@log_blueprint.route("/<int:log_id>", methods=["POST"])
def update_log(log_id: int):
    log_data = LogCreate(**request.form)
    db: Session = next(get_db())
    log_service = LogService(db)
    updated_log = log_service.update_log(
        log_id=log_id,
        message=log_data.message,
        timestamp=log_data.timestamp
    )
    if not updated_log:
        return jsonify({"message": "Log not found"}), 404
    return render_template("log/view.html", log=Log.from_orm(updated_log))

@log_blueprint.route("/<int:log_id>/delete", methods=["GET"])
def get_delete_log_form(log_id: int):
    db: Session = next(get_db())
    log_service = LogService(db)
    log = log_service.get_log_by_id(log_id)
    if not log:
        return jsonify({"message": "Log not found"}), 404
    return render_template("log/delete.html", log=Log.from_orm(log))

@log_blueprint.route("/<int:log_id>", methods=["DELETE"])
def delete_log(log_id: int):
    db: Session = next(get_db())
    log_service = LogService(db)
    if not log_service.delete_log(log_id):
        return jsonify({"message": "Log not found"}), 404
    return render_template("log/view.html")