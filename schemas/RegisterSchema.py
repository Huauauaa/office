from marshmallow import Schema, fields


class RegisterSchema(Schema):

    username = fields.Str(required=True)
    password = fields.Str(required=True)
