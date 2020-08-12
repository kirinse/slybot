from scrapy.exporters import CsvItemExporter
# from scrapy.conf import settings
from scrapy.utils.project import get_project_settings

class SlybotCSVItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        settings = get_project_settings()
        kwargs['fields_to_export'] = settings.getlist('CSV_EXPORT_FIELDS') or None
        super(SlybotCSVItemExporter, self).__init__(*args, **kwargs)
