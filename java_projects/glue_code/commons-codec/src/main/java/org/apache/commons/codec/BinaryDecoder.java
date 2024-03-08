package org.apache.commons.codec;


public interface BinaryDecoder extends Decoder {
  byte[] decode(byte[] source) throws DecoderException;
}
