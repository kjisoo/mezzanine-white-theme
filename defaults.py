from mezzanine.conf import register_setting

register_setting(
        name="GITHUB_NAME",
        label="github name",
        description="",
        editable=True,
        default='',
        )

register_setting(
    name="FACEBOOK_NAME",
    label="fackbook name",
    description="",
    editable=True,
    default='',
)

register_setting(
    name="LINKEDIN_NAME",
    label="linkedin name",
    description="",
    editable=True,
    default='',
)

register_setting(
    name="COPYRIGHT",
    label="copyright name",
    description="",
    editable=True,
    default='',
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    editable=False,
    default=("GITHUB_NAME", "FACEBOOK_NAME", "LINKDIN_NAME", "COPYRIGHT", ),
    append=True,
)
