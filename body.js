function get_uint8(flags, data4) {
    const bytes = new Uint8Array(data4.length + 5);
    bytes.set(data4, 5);
    const v3 = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
    return v3.setUint8(0, flags),
        v3.setUint32(1, data4.length),
        bytes
}

function get_body(dataJson) {
    var data4 = new TextEncoder().encode(JSON.stringify(dataJson))
    console.log(data4)
    return Array.from(get_uint8(0, data4))
}

