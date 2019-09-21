import a

print(f"in b: {__name__}")

if __name__ == "__main__":
    print("b wordt rechtstreeks uitgevoerd")
else:
    print("b wordt uitgevoerd door een import")
