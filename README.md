# Async Partial

Using async/await

## Example

**Terminal 1**
```bash
$ pdm run python src/server.py
```

**Terminal 2**
```bash
$ pdm run python src/client.py
```

**Terminal 3**
```bash
$ http GET :8001/fetch/test_1 number==3
```
