from __future__ import annotations

from flask import Blueprint, jsonify, request

audit_bp = Blueprint("audit_logs", __name__)

# Maintainer: นายนัธทวัฒน์ เขาแก้ว – Audit Log


@audit_bp.route("/", methods=["GET"])
def list_audit_logs():  # ดึงรายการ audit log พร้อม filter
    return jsonify(items=[]), 200


@audit_bp.route("/filters", methods=["GET"])
def audit_filters():  # ดึงรายการ action / user สำหรับตัวกรอง
    data = {
        "actions": [],
        "users": [],
    }
    return jsonify(data), 200

