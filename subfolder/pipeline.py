import conducto as co


def main() -> co.Serial:
    with co.Serial() as node:

        A = co.Image(dockerfile="Dockerfile", copy_repo=True)
        node["A context"] = co.Exec("ls /context", image=A)
        # - subfolder
        # - this_is_repo_root

        B = co.Image(dockerfile="Dockerfile", context=".", copy_repo=True)
        node["B context"] = co.Exec("ls /context", image=B)
        # - Dockerfile
        # - pipeline.py
        # - this_folder_containes_dockerfile

        C = co.Image(dockerfile="Dockerfile", context=".")
        node["C context"] = co.Exec("ls /context", image=C)
        # - Dockerfile
        # - pipeline.py
        # - this_folder_containes_dockerfile

    return node


if __name__ == "__main__":
    co.main(default=main)
