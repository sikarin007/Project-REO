from __future__ import annotations

from flask import Blueprint, jsonify, request

project_bp = Blueprint("projects", __name__)

# Maintainer: นายกฤษฎาพงษ์ ทิณพัฒน์  – Project CRUD


@project_bp.route("/", methods=["GET"])
def list_projects():  # ดึงรายการโครงการทั้งหมด (รองรับ filter)
    return jsonify(items=[]), 200


@project_bp.route("/<int:project_id>", methods=["GET"])
def get_project(project_id: int):  # ดึงรายละเอียดโครงการตาม ID
    return jsonify(project_id=project_id, data=None), 200


@project_bp.route("/", methods=["POST"])
def create_project():  # สร้างโครงการใหม่
    payload = request.get_json(silent=True) or {}
    return jsonify(message="create project placeholder", payload=payload), 201


@project_bp.route("/<int:project_id>", methods=["PUT"])
def update_project(project_id: int):  # แก้ไขข้อมูลโครงการ
    payload = request.get_json(silent=True) or {}
    return jsonify(message="update project placeholder", project_id=project_id, payload=payload), 200


@project_bp.route("/<int:project_id>", methods=["DELETE"])
def delete_project(project_id: int):  # ลบโครงการ
    return jsonify(message="delete project placeholder", project_id=project_id), 200


@project_bp.route("/<int:project_id>/images", methods=["POST"])
def upload_project_images(project_id: int):  # อัปโหลดรูปภาพของโครงการ
    return jsonify(message="upload project images placeholder", project_id=project_id), 201


@project_bp.route("/<int:project_id>/images/<int:image_id>", methods=["DELETE"])
def delete_project_image(project_id: int, image_id: int):  # ลบรูปภาพของโครงการ
    return jsonify(
        message="delete project image placeholder",
        project_id=project_id,
        image_id=image_id,
    ), 200

