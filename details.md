admin/
tasks/
users/ sign-up/ [name='sign-up']
users/ sign-in/ [name='sign-in']
users/ sign-out/ [name='logout']
users/ activate/<int:user_id>/<str:token>/
users/ admin/dashboard/ [name='admin-dashboard']
users/ admin/<int:user_id>/assign-role/ [name='assign-role']
users/ admin/create-group/ [name='create-group']
users/ admin/group-list/ [name='group-list']
users/ profile/ [name='profile']
users/ password-change/ [name='password_change']
users/ password-change/done/ [name='password_change_done']
users/ password-reset/ [name='password_reset']
users/ password-reset/confirm/<uidb64>/<token>/ [name='password_reset_confirm']
users/ edit-profile/ [name='edit_profile']
[name='home']
no-permission/ [name='no-permission']
features/ [name='features']
pricing/ [name='pricing']
about/ [name='about']
contact/ [name='contact']
^**debug**/
^media/(?P<path>.\*)$
