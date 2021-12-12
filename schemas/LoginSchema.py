from marshmallow import Schema, fields


class LoginSchema(Schema):

    username = fields.Str(required=True, error_messages={'required': 'required'})
    password = fields.Str(required=True)
