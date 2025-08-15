from extensions import db
from .user import User
from .property import Property
from .property_image import PropertyImage
from .lead import Lead
from .client_preference import ClientPreference
from .activity_log import ActivityLog
from .client_agent import ClientAgent
from .contact_log import ContactLog
from .saved_property import SavedProperty
from .viewing_request import ViewingRequest

def register_models():
    #his ensures models are imported and registered with SQLAlchemy

    pass