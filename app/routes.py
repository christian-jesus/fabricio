# app/routes.py
from flask import Blueprint, request, jsonify
from .recommendations import load_data, recommend_courses

main = Blueprint('main', __name__)
df = load_data()

@main.route('/recommend', methods=['GET'])
def recommend():
    course_name = request.args.get('course')
    recommendations = recommend_courses(course_name, df)
    return jsonify(recommendations)
