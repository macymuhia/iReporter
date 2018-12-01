class Config(object):

    DEBUG = False


class DevelopmentConfig(Config):

    DEBUG = True


class TestingConfig(Config):

    DEBUG = True
    TESTING = True


class ProductionConfig(Config):

    DEBUG = False
    TESTING = False


class StagingConfig(Config):

    DEBUG = True


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "staging": StagingConfig,
}
