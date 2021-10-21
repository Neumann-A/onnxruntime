# automatically generated by the FlatBuffers compiler, do not modify

# namespace: fbs

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class RuntimeOptimizationRecord(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRuntimeOptimizationRecord(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = RuntimeOptimizationRecord()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def RuntimeOptimizationRecordBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x4F\x52\x54\x4D", size_prefixed=size_prefixed)

    # RuntimeOptimizationRecord
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RuntimeOptimizationRecord
    def ActionId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # RuntimeOptimizationRecord
    def NodesToOptimizeIndexes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from ort_flatbuffers_py.experimental.fbs.NodesToOptimizeIndexes import NodesToOptimizeIndexes
            obj = NodesToOptimizeIndexes()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # RuntimeOptimizationRecord
    def ProducedNodeKernelDefHashes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # RuntimeOptimizationRecord
    def ProducedNodeKernelDefHashesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # RuntimeOptimizationRecord
    def ProducedNodeKernelDefHashesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # RuntimeOptimizationRecord
    def ProducedNodeKernelDefHashesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def RuntimeOptimizationRecordStart(builder): builder.StartObject(3)
def RuntimeOptimizationRecordAddActionId(builder, actionId): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(actionId), 0)
def RuntimeOptimizationRecordAddNodesToOptimizeIndexes(builder, nodesToOptimizeIndexes): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(nodesToOptimizeIndexes), 0)
def RuntimeOptimizationRecordAddProducedNodeKernelDefHashes(builder, producedNodeKernelDefHashes): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(producedNodeKernelDefHashes), 0)
def RuntimeOptimizationRecordStartProducedNodeKernelDefHashesVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def RuntimeOptimizationRecordEnd(builder): return builder.EndObject()
