# Error Codes

TWAMP error codes as defined in RFC 4656 (OWAMP) and used in RFC 5357 (TWAMP).

## Error Code Reference

| Code | Name | Description |
|:----:|------|-------------|
| 0 | **OK** | Success - No error occurred |
| 1 | **Failure** | Failure, reason unspecified (catch-all) |
| 2 | **Internal Error** | Internal error occurred in the implementation |
| 3 | **Not Supported** | Some aspect of the request is not supported |
| 4 | **Permanent Resource Limitation** | Cannot perform request due to permanent resource limitations |
| 5 | **Temporary Resource Limitation** | Cannot perform request due to temporary resource limitations |

## Error Code Details

### Code 0: OK

**Meaning**: The operation completed successfully.

**Action**: None required. This indicates normal operation.

**Example scenarios**:
- Connection established successfully
- Test session started successfully
- All packets transmitted and received

---

### Code 1: Failure (Unspecified)

**Meaning**: A general failure occurred, but the specific reason is not identified or does not fit other categories.

**Possible causes**:
- Network connectivity issues
- Unexpected protocol violations
- General communication errors

**Troubleshooting**:
1. Check network connectivity between endpoints
2. Verify firewall rules allow TWAMP traffic
3. Check logs for specific error messages
4. Verify both endpoints are using compatible TWAMP versions

---

### Code 2: Internal Error

**Meaning**: An internal error occurred within the TWAMP implementation.

**Possible causes**:
- Software bug
- Memory allocation failure
- System resource exhaustion
- Unexpected exception

**Troubleshooting**:
1. Check system logs for errors
2. Verify sufficient system resources (memory, CPU)
3. Try restarting the TWAMP process
4. Report bug if reproducible

---

### Code 3: Not Supported

**Meaning**: The requested feature or parameter is not supported by this implementation.

**Possible causes**:
- Requesting authenticated mode (not implemented in twampy)
- Requesting encrypted mode (not implemented)
- Using unsupported protocol features
- Incompatible protocol version

**Troubleshooting**:
1. Verify you're using unauthenticated mode
2. Check that both endpoints support the requested features
3. Review RFC 5357 for optional vs required features
4. Use compatible protocol parameters

**twampy specific limitations**:
- Only unauthenticated mode is supported
- Authenticated and encrypted modes return this error
- Some RFC 5938 and RFC 6038 features not supported

---

### Code 4: Permanent Resource Limitation

**Meaning**: The request cannot be performed due to permanent resource constraints.

**Possible causes**:
- Maximum number of concurrent sessions reached
- Insufficient port range available
- Hardware limitations
- License restrictions (commercial implementations)

**Troubleshooting**:
1. Reduce number of concurrent sessions
2. Check system configuration limits
3. Verify no port conflicts exist
4. Review system resource allocation

---

### Code 5: Temporary Resource Limitation

**Meaning**: The request cannot be performed right now due to temporary resource constraints, but may succeed if retried later.

**Possible causes**:
- Temporary memory shortage
- CPU overload
- Network buffer exhaustion
- Rate limiting

**Troubleshooting**:
1. Wait and retry the operation
2. Reduce packet rate or session count
3. Check system load (CPU, memory, network)
4. Implement exponential backoff for retries

---

## Error Handling Best Practices

### For Users

1. **Check error code**: Identify the specific error code returned
2. **Review logs**: Enable verbose or debug logging for details
3. **Verify configuration**: Ensure parameters are within supported ranges
4. **Test connectivity**: Verify network path to remote endpoint
5. **Retry appropriately**: For code 5, retry after a delay

### For Developers

1. **Log error details**: Include error code and context in logs
2. **Provide meaningful messages**: Translate error codes to user-friendly text
3. **Implement retries**: Automatically retry on code 5 errors
4. **Validate inputs**: Check parameters before sending requests
5. **Handle gracefully**: Don't crash on protocol errors

## Example Error Scenarios

### Scenario 1: Connection Refused

```bash
$ twampy controller 192.168.1.100
Error: Connection refused (Code 1)
```

**Cause**: No TWAMP server listening on the target

**Solution**:
```bash
# Verify server is running
netstat -ulnp | grep 862

# Start responder if needed
twampy responder :862
```

### Scenario 2: Authenticated Mode Not Supported

```bash
$ twampy controller 192.168.1.100
Error: Authenticated mode not supported (Code 3)
```

**Cause**: Server requires authentication, but twampy only supports unauthenticated mode

**Solution**: Configure server for unauthenticated mode or use a different client

### Scenario 3: Too Many Sessions

```bash
$ twampy controller 192.168.1.100
Error: Maximum sessions reached (Code 4)
```

**Cause**: Server has reached its session limit

**Solution**: Wait for existing sessions to complete or increase server session limit

### Scenario 4: Temporary Overload

```bash
$ twampy sender 192.168.1.100
Error: Temporary resource limitation (Code 5)
```

**Cause**: Server is temporarily overloaded

**Solution**: Retry after a brief delay

## Related References

- [RFC 4656 - OWAMP Protocol](https://tools.ietf.org/html/rfc4656) - Error code definitions
- [RFC 5357 - TWAMP Protocol](https://tools.ietf.org/html/rfc5357) - TWAMP-specific usage
- [Usage Guide](../user-guide/usage.md) - Practical usage examples
- [Configuration Guide](../user-guide/configuration.md) - Parameter reference
