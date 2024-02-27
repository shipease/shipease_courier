import xlsxwriter
import io
from django.http import HttpResponse


class XlsxHander:

    @staticmethod
    def get_workbook():
        # Create an in-memory Excel file
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()
        return workbook, worksheet, output

    @staticmethod
    def write_list_into_columns(worksheet, workbook, data_list,):
        for col_index, partner_pin_list in enumerate(data_list):

            # data = list(partner_pin_list['pin_list'])
            # data.insert(0, partner_pin_list['partner_name'])
            worksheet.write_column(0, col_index, partner_pin_list)

        workbook.close()
        return workbook, worksheet

    def return_file_response(output, file_name):
        # Set response headers for Excel file download
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{file_name}.xlsx"'

        # Write the Excel file contents to the response
        output.seek(0)
        response.write(output.getvalue())
        return response
