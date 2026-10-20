import pytest
from utils.text_data import TextData


NAME_DEPARTMENT = TextData.create_text_data("New Department")
NAME_DESIGNATION = TextData.create_text_data("New Designation")
NAME_POLICIES = TextData.create_text_data("New Policies")

def test_create_department(logged_in_department):
    logged_in_department.go_to_department_page()
    logged_in_department.create_department(NAME_DEPARTMENT)
    logged_in_department.verify_create_success(NAME_DEPARTMENT)

def test_create_designation(logged_in_designation):
    logged_in_designation.go_to_department_page()
    logged_in_designation.create_department(NAME_DESIGNATION)
    logged_in_designation.verify_create_success(NAME_DESIGNATION)

def test_create_policies(logged_in_policy):
    logged_in_policy.go_to_department_page()
    logged_in_policy.create_department(NAME_POLICIES)
    logged_in_policy.verify_create_success(NAME_POLICIES)