class ParameterValidatorImpl:

    @staticmethod
    def validateParameter(bean, form, field, validator, action, results, locale) -> bool:
        try:
            return True
        except Exception as e:
            raise e
