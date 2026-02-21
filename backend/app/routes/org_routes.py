from __future__ import annotations

from flask import Blueprint, jsonify, request

org_bp = Blueprint("orgs", __name__)

# Maintainer: นายศิขรินทร์ ภูติโส – Organization Management


@org_bp.route("/", methods=["GET"])
def list_orgs():  # ดึงรายการหน่วยงานทั้งหมด (สำหรับ Admin)
    return jsonify(items=[]), 200


@org_bp.route("/public", methods=["GET"])
def list_orgs_public():  # ดึงรายการหน่วยงานแบบ read-only (สำหรับผู้ใช้ทั่วไป)
    return jsonify(items=[]), 200


@org_bp.route("/", methods=["POST"])
def create_org():  # เพิ่มหน่วยงานใหม่
    payload = request.get_json(silent=True) or {}
    return jsonify(message="create org placeholder", payload=payload), 201


@org_bp.route("/<int:org_id>", methods=["PUT"])
def update_org(org_id: int):  # แก้ไขข้อมูลหน่วยงาน (เช่น ชื่อ/สถานะ)
    payload = request.get_json(silent=True) or {}
    return jsonify(message="update org placeholder", org_id=org_id, payload=payload), 200


@org_bp.route("/<int:org_id>", methods=["DELETE"])
def delete_org(org_id: int):  # ลบหน่วยงาน (ต้องไม่มีข้อมูลเกี่ยวข้อง)
    return jsonify(message="delete org placeholder", org_id=org_id), 200


@org_bp.route("/<int:org_id>/cascade", methods=["DELETE"])
def delete_org_cascade(org_id: int):  # ลบหน่วยงานพร้อมโครงการ/ผู้ใช้ที่เกี่ยวข้อง
    return jsonify(message="delete org cascade placeholder", org_id=org_id), 200

