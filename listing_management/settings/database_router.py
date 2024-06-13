
from listing_management.settings.config import DATABASE_MAPPING
from listing_management.settings.constants import APP_NAME, DB_EVENT_STORE, DB_READ_MODEL


class EventStoreRouter:
    def __valid_model(self, app_label, model_name):
        if app_label not in APP_NAME:
            return False

        if model_name not in DATABASE_MAPPING[DB_EVENT_STORE]:
            return False
        
        return True

    def db_for_read(self, model, **hints):
        if not self.__valid_model(model._meta.app_label, model._meta.model_name):
            return None
        
        return DB_EVENT_STORE

    def db_for_write(self, model, **hints):
        if not self.__valid_model(model._meta.app_label, model._meta.model_name):
            return None
        
        return DB_EVENT_STORE

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if not self.__valid_model(app_label, model_name):
            return None
        
        return DB_EVENT_STORE
        

class ReadModelRouter:
    def __valid_model(self, app_label, model_name):
        if app_label not in APP_NAME:
            return False

        if model_name not in DATABASE_MAPPING[DB_READ_MODEL]:
            return False
        
        return True

    def db_for_read(self, model, **hints):
        if not self.__valid_model(model._meta.app_label, model._meta.model_name):
            return None
        
        return DB_READ_MODEL

    def db_for_write(self, model, **hints):
        if not self.__valid_model(model._meta.app_label, model._meta.model_name):
            return None
        
        return DB_READ_MODEL

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if not self.__valid_model(app_label, model_name):
            return None
        
        return DB_READ_MODEL
        