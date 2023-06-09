from rest_framework import status

from tests.test_icd.test_setup import (
    CategoryTestSetup,
    DiagnosisTestSetup,
    FileTestSetup,
)


class CategoryViewsTest(CategoryTestSetup):
    def test_list_categories(self):
        response = self.client.get(self.category_list_create_url, format="json")

        expected_data = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {"id": 1, "category_code": "A01", "category_title": "Category 1"},
                {"id": 2, "category_code": "B01", "category_title": "Category 2"},
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_data)

    def test_add_category(self):
        data = {"category_code": "C01", "category_title": "Category 3"}
        response = self.client.post(
            self.category_list_create_url,
            data=data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_add_category_with_existing_category_code(self):
        data = {"category_code": "A01", "category_title": "Category 3"}
        response = self.client.post(
            self.category_list_create_url,
            data=data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()["category_code"], ["Cateogory code already exists"]
        )

    def test_cannot_add_category_with_existing_caseinsensitive_category_code(self):
        data = {"category_code": "a01", "category_title": "Category 3"}
        response = self.client.post(
            self.category_list_create_url,
            data=data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()["category_code"], ["Cateogory code already exists"]
        )

    def test_get_category(self):
        response = self.client.get(self.category_detail_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_category(self):
        data = {"category_code": "Z01", "category_title": "Category 26"}
        response = self.client.patch(self.category_detail_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        response = self.client.delete(self.category_detail_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class DiagnosisViewTest(DiagnosisTestSetup):
    def test_list_diagnosis(self):
        response = self.client.get(self.diagnosis_list_create_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_diagnosis(self):
        data = {
            "icd_type": "ICD_9",
            "category": 1,
            "diagnosis_code": 1,
            "abbreviated_desc": "Abbreviated Description 1",
            "full_desc": "Full Description 2",
        }
        response = self.client.post(
            self.diagnosis_list_create_url, data=data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_diagnosis(self):
        response = self.client.get(self.diagnosis_detail_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_diagnosis(self):
        data = {
            "icd_type": "ICD_9",
            "category": 1,
            "diagnosis_code": 2,
            "abbreviated_desc": "Abbreviated Description 1",
            "full_desc": "Full Description 2",
        }
        response = self.client.patch(self.diagnosis_detail_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_diagnosis(self):
        response = self.client.delete(self.diagnosis_detail_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FileViewTest(FileTestSetup):
    def test_add_file(self):
        data = {
            "record_type": "Category",
            "file": open(self.storage.path(self.category_csv_file), "rb"),
        }

        response = self.client.post(self.file_upload_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
