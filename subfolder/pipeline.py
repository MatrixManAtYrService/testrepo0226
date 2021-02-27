import conducto as co


def main() -> co.Serial:
    with co.Serial() as node:

        B = co.Image(dockerfile="Dockerfile", context=".", copy_repo=True)
        node["B context"] = co.Exec("ls /context", image=B)
        # - Dockerfile
        # - pipeline.py
        # - this_folder_containes_dockerfile

    return node


if __name__ == "__main__":
    co.main(default=main)
