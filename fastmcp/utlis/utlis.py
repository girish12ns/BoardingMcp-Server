import base64


#creating usernmae ,password and project_id
def generate_new_token(username, password, project_id):
    try:
        if not all([username, password, project_id]):
            raise ValueError("Username, password, and project_id cannot be empty")
        
        if any(':' in str(param) for param in [username, password, project_id]):
            raise ValueError("Username, password, and project_id cannot contain colons")
        
        raw_string = f"{username}:{password}:{project_id}"
        token = base64.b64encode(raw_string.encode("utf-8")).decode("utf-8")
        return token
        
    except ValueError as ve:
        print(f"Validation Error: {ve}")
        return None
        
    except Exception as e:
        print(f"Unexpected error generating token: {e}")
        return None


# token = generate_token("john_doe", "secret123", "proj_456")
# if token:
#     print(f"Token generated: {token}")