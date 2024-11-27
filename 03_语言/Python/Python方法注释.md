

方法的头部注释，可以参考下面的模板（ChatGPT生成的写得挺好的）

```java

def delete_release_note(owner, repo, release_id, token):
    """
    Delete a GitHub release by release_id.

    Parameters:
    - owner (str): GitHub username or organization name.
    - repo (str): Repository name.
    - release_id (int): ID of the release to delete.
    - token (str): GitHub personal access token for authentication.

    Returns:
    - bool: True if deletion is successful, False otherwise.
    """

    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{repo}/releases/{release_id}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Release with ID {release_id} deleted successfully.")
        return True
    else:
        print(f"Failed to delete release with ID {release_id}.")
        return False

```

