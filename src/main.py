def handler(event, context):
    try:
        a = int(event.get('a'))
        b = int(event.get('b'))

        print(f"a + b: {a + b}")
        print(f"a - b: {a - b}")
        print(f"a * b: {a * b}")
        print(f"a // b: {a // b}")
        
        return {
            "add": a + b,
            "sub": a - b,
            "mul": a * b,
            "div": a // b
        }
    except Exception as e:
        return {"error": str(e)}
