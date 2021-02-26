import conducto as co

img = co.Image(dockerfile="./Dockerfile", context=".", copy_repo=True)

def main() -> co.Serial:
    with co.Serial(image=img) as node:
        node["showroot"] = co.Exec("ls /")
        node["showchild"] = co.Exec("ls /child")
    return node


if __name__ == "__main__":
    co.main(default=main)
