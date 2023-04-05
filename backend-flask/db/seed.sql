INSERT INTO public.users (display_name, handle, cognito_user_id)
VALUES
  ('Andrew Brown', 'test@email.com', 'andrewbrown' ,'MOCK'),
  ('Andrew Bayko', 'test@email.com', 'bayko' ,'MOCK');

INSERT INTO public.activities (uuid, message, expires_at)
VALUES
  (
    (SELECT user_uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )