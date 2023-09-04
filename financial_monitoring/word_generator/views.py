import os
from rest_framework.views import APIView
from docx import Document
from io import BytesIO
from django.http import HttpResponse
from datetime import date
from rest_framework.response import Response
from general_info.serializers import GeneralInfoSerializer
from general_info.models import GeneralInfo
from datetime import datetime


class GenerateDocumentView(APIView):

    month_names = {
        "1": "Января",
        "2": "Февраля",
        "3": "Марта",
        "4": "Апреля",
        "5": "Мая",
        "6": "Июня",
        "7": "Июля",
        "8": "Августа",
        "9": "Сентября",
        "10": "Октября",
        "11": "Ноября",
        "12": "Декабря",
    }

    def post(self, request, iin, *args, **kwargs):
        user = GeneralInfoSerializer(GeneralInfo.objects.get(iin=iin))

        template_path = "word_generator/static/templates/template.docx"
        template_doc = Document(template_path)

        date1 = datetime.strptime(
            request.data["date_depart"], "%Y-%m-%d").date()
        date2 = datetime.strptime(
            request.data["date_return"], "%Y-%m-%d").date()

        date_difference = date2 - date1
        number_of_days = str(date_difference.days)

        name = user.data["firstname"]
        surname = user.data["surname"]
        patronymic = user.data["patronymic"]
        order_type = request.data.get('order_type', None)
        type_of_order_type = request.data.get('type_of_order_type', None)

        day_depart = str(date1.day)
        month_depart = self.month_names[str(date1.month)]
        year_depart = str(date1.year)

        day_return = str(date2.day)
        month_return = self.month_names[str(date2.month)]
        year_return = str(date2.year)

        current_date = datetime.now()
        current_day = str(current_date.day)
        current_month = self.month_names[str(current_date.month)]
        current_year = str(current_date.year)

        name_placehoder = "name"
        surname_placehoder = "surname"
        patronymic_placeholder = "patronymic"
        order_type_placehoder = "ordertype"
        type_of_order_type_placeholder = "typeof"
        counts_day_placeholder = "count"

        day_depart_placeholder = "daydepart"
        month_depart_placeholder = "monthdepart"
        year_depart_placeholder = "yeardepart"

        day_return_placeholder = "dayreturn"
        month_return_placeholder = "monthreturn"
        year_return_placeholder = "yearreturn"

        day_now_placeholder = "daynow"
        month_now_placeholder = "monthnow"
        year_now_placeholder = "yearnow"

        for paragraph in template_doc.paragraphs:
            for run in paragraph.runs:
                run.text = run.text.replace(surname_placehoder, surname)
                run.text = run.text.replace(name_placehoder, name)
                run.text = run.text.replace(patronymic_placeholder, patronymic)
                run.text = run.text.replace(order_type_placehoder, order_type)

                if type_of_order_type is not None:
                    run.text = run.text.replace(
                        type_of_order_type_placeholder, type_of_order_type)
                else:
                    run.text = run.text.replace(
                        type_of_order_type_placeholder, "")

                run.text = run.text.replace(
                    counts_day_placeholder, number_of_days)

                run.text = run.text.replace(day_depart_placeholder, day_depart)
                run.text = run.text.replace(
                    month_depart_placeholder, month_depart)
                run.text = run.text.replace(
                    year_depart_placeholder, year_depart)

                run.text = run.text.replace(day_return_placeholder, day_return)
                run.text = run.text.replace(
                    month_return_placeholder, month_return)
                run.text = run.text.replace(
                    year_return_placeholder, year_return)

                run.text = run.text.replace(day_now_placeholder, current_day)
                run.text = run.text.replace(
                    month_now_placeholder, current_month)
                run.text = run.text.replace(year_now_placeholder, current_year)

        modified_template_buffer = BytesIO()
        template_doc.save(modified_template_buffer)
        modified_template_buffer.seek(0)

        response = HttpResponse(
            modified_template_buffer,
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename=Modified_Template.docx'

        return response

    # def get(self, request, *args, **kwargs):
    #     template_path = "word_generator/static/templates/template.docx"

    #     with open(template_path, 'rb') as template_file:
    #         template_content = template_file.read()
    #         print(template_content)

    #     response = HttpResponse(template_content,
    #                             content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    #     response['Content-Disposition'] = 'attachment; filename=Template.docx'

    #     return response
