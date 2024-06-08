from pathlib import Path

from listing_management.settings.constants import DB_EVENT_STORE, DB_READ_MODEL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent



DATABASE_MAPPING = {
    DB_EVENT_STORE: [
        "listingeventstore",
    ]
} 

DATABASE_ROUTERS = [
    "listing_management.settings.database_router.EventStoreRouter",
]

DATABASES = {
    DB_READ_MODEL: {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'read_model.sqlite3',
    },
    DB_EVENT_STORE: {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'event_store.sqlite3',
        "TEST": {
            "DEPENDENCIES": [],
            'NAME': BASE_DIR / 'event_store2.sqlite3',
        },
    },
}