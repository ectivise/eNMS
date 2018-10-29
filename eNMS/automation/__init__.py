from flask import Blueprint

bp = Blueprint(
    'automation_blueprint',
    __name__,
    url_prefix='/automation',
    template_folder='templates',
    static_folder='static'
)

from eNMS.base.classes import classes
from eNMS.automation.models import Job, Service, Workflow

classes.update({'Job': Job, 'Service': Service, 'Workflow': Workflow})

def create_service_classes():
    path_services = Path.cwd() / 'eNMS' / 'automation' / 'services'
    for file in path_services.glob('**/*.py'):
        if 'init' not in str(file):
            spec = spec_from_file_location(str(file), str(file))
            spec.loader.exec_module(module_from_spec(spec))
    for cls_name, cls in service_classes.items():
        for col in cls.__table__.columns:
            service_properties[cls_name].append(col.key)
            service_import_properties.append(col.key)
            if type(col.type) == Boolean:
                boolean_properties.append(col.key)
            if (
                type(col.type) == PickleType
                and hasattr(cls, f'{col.key}_values')
            ):
                property_types[col.key] = list
            else:
                property_types[col.key] = {
                    Boolean: bool,
                    Integer: int,
                    Float: float,
                    PickleType: dict,
                }.get(type(col.type), str)

create_service_classes()
classes.update(service_classes)

import eNMS.automation.routes  # noqa: F401
