from __future__ import annotations

from flask import Blueprint, jsonify, request

user_bp = Blueprint("users", __name__)

# Maintainer: นายพิชชากร คำพรม – User & Role Management


@user_bp.route("/", methods=["GET"])
def list_users():  # ดึงรายการผู้ใช้ทั้งหมด (สำหรับ Admin)
    return jsonify(items=[]), 200


@user_bp.route("/", methods=["POST"])
def create_user():  # เพิ่มผู้ใช้ใหม่
    payload = request.get_json(silent=True) or {}
    return jsonify(message="create user placeholder", payload=payload), 201


@user_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id: int):  # แก้ไขข้อมูลทั่วไปและบทบาทของผู้ใช้
    payload = request.get_json(silent=True) or {}
    return jsonify(
        message="update user placeholder",
        user_id=user_id,
        payload=payload,
    ), 200


@user_bp.route("/<int:user_id>/password", methods=["PUT"])
def change_user_password(user_id: int):  # เปลี่ยนรหัสผ่านของผู้ใช้
    payload = request.get_json(silent=True) or {}
    return jsonify(
        message="change user password placeholder",
        user_id=user_id,
        payload=payload,
    ), 200

