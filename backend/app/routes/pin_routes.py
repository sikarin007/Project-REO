from __future__ import annotations

from flask import Blueprint, jsonify, request

pin_bp = Blueprint("org_pins", __name__)

# Maintainer: นายพิชชากร คำพรม – Org PIN management


@pin_bp.route("/<int:org_id>/pin", methods=["PUT"])
def set_org_pin(org_id: int):  # ตั้งค่าหรือรีเซ็ต PIN ของหน่วยงานที่ระบุ
    return jsonify(message="set org pin placeholder", org_id=org_id), 200


@pin_bp.route("/pins/reset-all", methods=["POST"])
def reset_all_org_pins():  # รีเซ็ต PIN ของทุกหน่วยงานเป็นค่าเริ่มต้น
    return jsonify(message="reset all org pins placeholder"), 200

