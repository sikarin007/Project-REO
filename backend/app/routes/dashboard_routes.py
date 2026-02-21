from __future__ import annotations

from flask import Blueprint, jsonify

dashboard_bp = Blueprint("dashboard", __name__)

# Maintainer: นายไชยวัฒน์ ทำดี – Dashboard


@dashboard_bp.route("/summary", methods=["GET"])
def summary():  # สรุปจำนวนโครงการ งบประมาณ และหน่วยงาน
    data = {
        "total_projects": 0,
        "total_budget": 0,
        "total_orgs": 0,
    }
    return jsonify(data), 200


@dashboard_bp.route("/by-org", methods=["GET"])
def by_org():  # สรุปข้อมูลโครงการตามหน่วยงาน
    return jsonify(items=[]), 200


@dashboard_bp.route("/by-sdg", methods=["GET"])
def by_sdg():  # สรุปจำนวนโครงการตาม SDG Target
    return jsonify(items=[]), 200

