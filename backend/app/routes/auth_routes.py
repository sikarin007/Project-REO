from __future__ import annotations

from flask import Blueprint, jsonify, request

auth_bp = Blueprint("auth", __name__)

# Maintainer: นายอัครพนธ์ โอมาโฮนี่ – Login / Authentication


@auth_bp.route("/login", methods=["POST"])
def login():  # เข้าสู่ระบบด้วยหน่วยงาน + PIN
    return jsonify(message="login route placeholder"), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():  # ออกจากระบบ ล้าง session
    return jsonify(message="logout route placeholder"), 200


@auth_bp.route("/me", methods=["GET"])
def current_user():  # ดึงข้อมูลผู้ใช้ที่ล็อกอินอยู่
    return jsonify(user=None), 200
