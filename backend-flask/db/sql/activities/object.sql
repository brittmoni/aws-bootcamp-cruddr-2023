SELECT activities.uuid,
    users.display_name,
    users.handle,
    activities.message, 
    activities.created_at, 
    activities.expires_at,
FROM public.activities
INNER JOIN public.users ON users.uuid = activities.uuid
WHERE activities.uuid = %(uuid)s

-- On line 8, in the original code, activities.uuid was activities.user_uuid