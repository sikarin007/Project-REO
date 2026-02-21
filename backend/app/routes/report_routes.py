from __future__ import annotations

from flask import Blueprint, jsonify

report_bp = Blueprint("reports", __name__)

# Maintainer: นายไชยวัฒน์ ทำดี – รายงาน / Export


@report_bp.route("/export", methods=["GET"])
def export_projects():  # ส่งออกข้อมูลโครงการเป็นไฟล์ (เช่น CSV)
    return jsonify(message="export projects placeholder"), 200

