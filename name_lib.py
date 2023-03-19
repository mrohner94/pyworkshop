def upper_case_name(name):
    return name.upper()


if __name__ == "__main__":
    name = "Mike"
    new_name = upper_case_name(name)
    print(f"Upper case name is {new_name}")
print("dunder name", __name__)