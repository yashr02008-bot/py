# Topic: Check valid identifiers
import keyword
for word in ["name", "2name", "my_var", "my-var", "class", "_x"]:
    ok = word.isidentifier() and not keyword.iskeyword(word)
    print(word, "->", "valid" if ok else "invalid")
