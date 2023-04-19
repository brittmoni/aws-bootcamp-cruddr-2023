INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Andrew Brown', 'test@email.com', 'andrewbrown' , 'MOCK'),
  ('Andrew Bayko', 'test@email.com', 'bayko' , 'MOCK'),
  ('Britt', 'test@email.com', 'Britt', '226f7e4d-a5dd-42d3-a357-1b7efec16d23'),
  ('Tiff', 'test@email.com', 'Tiff', 'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )