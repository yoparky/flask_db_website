from flask import flash

def flashMessage(attribute='', charCount=0, crud=''):
    if crud == 'create':
        flash(f"Entry added!", category='success')
    elif crud == 'update':
        flash(f"Entry updated!", category='success')
    else: 
        flash(f"{attribute} must be greater than {charCount} character(s)", category='error')
