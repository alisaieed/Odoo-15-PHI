{
    'name': "Arabic Theme",
    'description': """Applying the arabic font family (Cairo) to the standard theme""",
    'category': 'Theme',
    'summary': 'Change the theme language to arabic',
    'version': '1.0',
    'depends': ['base'],
    'data': [],
    'author': "T2 Team",
    'assets': {
        'web.assets_backend': [
                'arabic_theme/static/src/css/style.css',
        ],
        'web.report_assets_common': [
            'arabic_theme/static/src/css/report_style.css',
        ],
    },
}