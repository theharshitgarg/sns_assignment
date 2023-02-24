Django Intern Assignment
• Create the following backend structure
1) Client table
▪ Name
▪ User Instance (Foreign Key)
2) Artist Table
▪ Name
▪ Work (ManyToManyField)
3) Work Table
▪ Link
▪ Work Type
• Youtube
• Instagram
• Other
◦* Important
▪ After each ‘Registration’ for a new user
▪ Make sure a new Client object is created using signals
• Rest API
◦ Integrate API endpoint for showing
▪ Works
▪ Integrate Filtering with Work Type
▪ Integrate Search with Artist name
▪ Integrate Registration API with username & password
within the body of the request
Example:
http://127.0.0.1:8000/api/works
http://127.0.0.1:8000/api/works?artist=[Artist Name]
http://127.0.0.1:8000/api/works?work_type=Youtube or pk of
YouTube
http://127.0.0.1:8000/api/register
where body = {username: ”testuser”, password: 123123}
• Note
▪ Make a git repository and upload the code there. Make
sure to add a README explaining your API endpoints