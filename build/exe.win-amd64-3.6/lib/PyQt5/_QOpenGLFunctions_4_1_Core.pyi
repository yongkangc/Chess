# The PEP 484 type hints stub file for the _QOpenGLFunctions_4_1_Core module.
#
# Generated by SIP 4.18.1
#
# Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt5 import QtGui

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QOpenGLFunctions_4_1_Core(QtGui.QAbstractOpenGLFunctions):

    def __init__(self) -> None: ...

    def glReleaseShaderCompiler(self) -> None: ...
    def glDepthRangef(self, n: float, f: float) -> None: ...
    def glClearDepthf(self, dd: float) -> None: ...
    def glProgramParameteri(self, program: int, pname: int, value: int) -> None: ...
    def glUseProgramStages(self, pipeline: int, stages: int, program: int) -> None: ...
    def glActiveShaderProgram(self, pipeline: int, program: int) -> None: ...
    def glBindProgramPipeline(self, pipeline: int) -> None: ...
    def glIsProgramPipeline(self, pipeline: int) -> int: ...
    def glProgramUniform1i(self, program: int, location: int, v0: int) -> None: ...
    def glProgramUniform1f(self, program: int, location: int, v0: float) -> None: ...
    def glProgramUniform1d(self, program: int, location: int, v0: float) -> None: ...
    def glProgramUniform1ui(self, program: int, location: int, v0: int) -> None: ...
    def glProgramUniform2i(self, program: int, location: int, v0: int, v1: int) -> None: ...
    def glProgramUniform2f(self, program: int, location: int, v0: float, v1: float) -> None: ...
    def glProgramUniform2d(self, program: int, location: int, v0: float, v1: float) -> None: ...
    def glProgramUniform2ui(self, program: int, location: int, v0: int, v1: int) -> None: ...
    def glProgramUniform3i(self, program: int, location: int, v0: int, v1: int, v2: int) -> None: ...
    def glProgramUniform3f(self, program: int, location: int, v0: float, v1: float, v2: float) -> None: ...
    def glProgramUniform3d(self, program: int, location: int, v0: float, v1: float, v2: float) -> None: ...
    def glProgramUniform3ui(self, program: int, location: int, v0: int, v1: int, v2: int) -> None: ...
    def glProgramUniform4i(self, program: int, location: int, v0: int, v1: int, v2: int, v3: int) -> None: ...
    def glProgramUniform4f(self, program: int, location: int, v0: float, v1: float, v2: float, v3: float) -> None: ...
    def glProgramUniform4d(self, program: int, location: int, v0: float, v1: float, v2: float, v3: float) -> None: ...
    def glProgramUniform4ui(self, program: int, location: int, v0: int, v1: int, v2: int, v3: int) -> None: ...
    def glValidateProgramPipeline(self, pipeline: int) -> None: ...
    def glVertexAttribL1d(self, index: int, x: float) -> None: ...
    def glVertexAttribL2d(self, index: int, x: float, y: float) -> None: ...
    def glVertexAttribL3d(self, index: int, x: float, y: float, z: float) -> None: ...
    def glVertexAttribL4d(self, index: int, x: float, y: float, z: float, w: float) -> None: ...
    def glViewportIndexedf(self, index: int, x: float, y: float, w: float, h: float) -> None: ...
    def glScissorIndexed(self, index: int, left: int, bottom: int, width: int, height: int) -> None: ...
    def glDepthRangeIndexed(self, index: int, n: float, f: float) -> None: ...
    def glMinSampleShading(self, value: float) -> None: ...
    def glBlendEquationi(self, buf: int, mode: int) -> None: ...
    def glBlendEquationSeparatei(self, buf: int, modeRGB: int, modeAlpha: int) -> None: ...
    def glBlendFunci(self, buf: int, src: int, dst: int) -> None: ...
    def glBlendFuncSeparatei(self, buf: int, srcRGB: int, dstRGB: int, srcAlpha: int, dstAlpha: int) -> None: ...
    def glUniform1d(self, location: int, x: float) -> None: ...
    def glUniform2d(self, location: int, x: float, y: float) -> None: ...
    def glUniform3d(self, location: int, x: float, y: float, z: float) -> None: ...
    def glUniform4d(self, location: int, x: float, y: float, z: float, w: float) -> None: ...
    def glPatchParameteri(self, pname: int, value: int) -> None: ...
    def glBindTransformFeedback(self, target: int, id: int) -> None: ...
    def glIsTransformFeedback(self, id: int) -> int: ...
    def glPauseTransformFeedback(self) -> None: ...
    def glResumeTransformFeedback(self) -> None: ...
    def glDrawTransformFeedback(self, mode: int, id: int) -> None: ...
    def glDrawTransformFeedbackStream(self, mode: int, id: int, stream: int) -> None: ...
    def glBeginQueryIndexed(self, target: int, index: int, id: int) -> None: ...
    def glEndQueryIndexed(self, target: int, index: int) -> None: ...
    def glVertexAttribDivisor(self, index: int, divisor: int) -> None: ...
    def glIsSampler(self, sampler: int) -> int: ...
    def glBindSampler(self, unit: int, sampler: int) -> None: ...
    def glSamplerParameteri(self, sampler: int, pname: int, param: int) -> None: ...
    def glSamplerParameterf(self, sampler: int, pname: int, param: float) -> None: ...
    def glQueryCounter(self, id: int, target: int) -> None: ...
    def glVertexP2ui(self, type: int, value: int) -> None: ...
    def glVertexP3ui(self, type: int, value: int) -> None: ...
    def glVertexP4ui(self, type: int, value: int) -> None: ...
    def glTexCoordP1ui(self, type: int, coords: int) -> None: ...
    def glTexCoordP2ui(self, type: int, coords: int) -> None: ...
    def glTexCoordP3ui(self, type: int, coords: int) -> None: ...
    def glTexCoordP4ui(self, type: int, coords: int) -> None: ...
    def glMultiTexCoordP1ui(self, texture: int, type: int, coords: int) -> None: ...
    def glMultiTexCoordP2ui(self, texture: int, type: int, coords: int) -> None: ...
    def glMultiTexCoordP3ui(self, texture: int, type: int, coords: int) -> None: ...
    def glMultiTexCoordP4ui(self, texture: int, type: int, coords: int) -> None: ...
    def glNormalP3ui(self, type: int, coords: int) -> None: ...
    def glColorP3ui(self, type: int, color: int) -> None: ...
    def glColorP4ui(self, type: int, color: int) -> None: ...
    def glSecondaryColorP3ui(self, type: int, color: int) -> None: ...
    def glVertexAttribP1ui(self, index: int, type: int, normalized: int, value: int) -> None: ...
    def glVertexAttribP2ui(self, index: int, type: int, normalized: int, value: int) -> None: ...
    def glVertexAttribP3ui(self, index: int, type: int, normalized: int, value: int) -> None: ...
    def glVertexAttribP4ui(self, index: int, type: int, normalized: int, value: int) -> None: ...
    def glFramebufferTexture(self, target: int, attachment: int, texture: int, level: int) -> None: ...
    def glProvokingVertex(self, mode: int) -> None: ...
    def glTexImage2DMultisample(self, target: int, samples: int, internalformat: int, width: int, height: int, fixedsamplelocations: int) -> None: ...
    def glTexImage3DMultisample(self, target: int, samples: int, internalformat: int, width: int, height: int, depth: int, fixedsamplelocations: int) -> None: ...
    def glSampleMaski(self, index: int, mask: int) -> None: ...
    def glDrawArraysInstanced(self, mode: int, first: int, count: int, instancecount: int) -> None: ...
    def glTexBuffer(self, target: int, internalformat: int, buffer: int) -> None: ...
    def glPrimitiveRestartIndex(self, index: int) -> None: ...
    def glUniformBlockBinding(self, program: int, uniformBlockIndex: int, uniformBlockBinding: int) -> None: ...
    def glColorMaski(self, index: int, r: int, g: int, b: int, a: int) -> None: ...
    def glEnablei(self, target: int, index: int) -> None: ...
    def glDisablei(self, target: int, index: int) -> None: ...
    def glIsEnabledi(self, target: int, index: int) -> int: ...
    def glBeginTransformFeedback(self, primitiveMode: int) -> None: ...
    def glEndTransformFeedback(self) -> None: ...
    def glBindBufferBase(self, target: int, index: int, buffer: int) -> None: ...
    def glClampColor(self, target: int, clamp: int) -> None: ...
    def glBeginConditionalRender(self, id: int, mode: int) -> None: ...
    def glEndConditionalRender(self) -> None: ...
    def glUniform1ui(self, location: int, v0: int) -> None: ...
    def glUniform2ui(self, location: int, v0: int, v1: int) -> None: ...
    def glUniform3ui(self, location: int, v0: int, v1: int, v2: int) -> None: ...
    def glUniform4ui(self, location: int, v0: int, v1: int, v2: int, v3: int) -> None: ...
    def glClearBufferfi(self, buffer: int, drawbuffer: int, depth: float, stencil: int) -> None: ...
    def glIsRenderbuffer(self, renderbuffer: int) -> int: ...
    def glBindRenderbuffer(self, target: int, renderbuffer: int) -> None: ...
    def glRenderbufferStorage(self, target: int, internalformat: int, width: int, height: int) -> None: ...
    def glIsFramebuffer(self, framebuffer: int) -> int: ...
    def glBindFramebuffer(self, target: int, framebuffer: int) -> None: ...
    def glCheckFramebufferStatus(self, target: int) -> int: ...
    def glFramebufferTexture1D(self, target: int, attachment: int, textarget: int, texture: int, level: int) -> None: ...
    def glFramebufferTexture2D(self, target: int, attachment: int, textarget: int, texture: int, level: int) -> None: ...
    def glFramebufferTexture3D(self, target: int, attachment: int, textarget: int, texture: int, level: int, zoffset: int) -> None: ...
    def glFramebufferRenderbuffer(self, target: int, attachment: int, renderbuffertarget: int, renderbuffer: int) -> None: ...
    def glGenerateMipmap(self, target: int) -> None: ...
    def glBlitFramebuffer(self, srcX0: int, srcY0: int, srcX1: int, srcY1: int, dstX0: int, dstY0: int, dstX1: int, dstY1: int, mask: int, filter: int) -> None: ...
    def glRenderbufferStorageMultisample(self, target: int, samples: int, internalformat: int, width: int, height: int) -> None: ...
    def glFramebufferTextureLayer(self, target: int, attachment: int, texture: int, level: int, layer: int) -> None: ...
    def glBindVertexArray(self, array: int) -> None: ...
    def glIsVertexArray(self, array: int) -> int: ...
    def glBlendEquationSeparate(self, modeRGB: int, modeAlpha: int) -> None: ...
    def glDrawBuffers(self, n: int, bufs: PYQT_OPENGL_ARRAY) -> None: ...
    def glStencilOpSeparate(self, face: int, sfail: int, dpfail: int, dppass: int) -> None: ...
    def glStencilFuncSeparate(self, face: int, func: int, ref: int, mask: int) -> None: ...
    def glStencilMaskSeparate(self, face: int, mask: int) -> None: ...
    def glAttachShader(self, program: int, shader: int) -> None: ...
    def glBindAttribLocation(self, program: int, index: int, name: str) -> None: ...
    def glCompileShader(self, shader: int) -> None: ...
    def glCreateProgram(self) -> int: ...
    def glCreateShader(self, type: int) -> int: ...
    def glDeleteProgram(self, program: int) -> None: ...
    def glDeleteShader(self, shader: int) -> None: ...
    def glDetachShader(self, program: int, shader: int) -> None: ...
    def glDisableVertexAttribArray(self, index: int) -> None: ...
    def glEnableVertexAttribArray(self, index: int) -> None: ...
    def glGetActiveAttrib(self, program: int, index: int) -> typing.Tuple[str, int, int]: ...
    def glGetActiveUniform(self, program: int, index: int) -> typing.Tuple[str, int, int]: ...
    def glGetAttachedShaders(self, program: int) -> typing.Tuple[int, ...]: ...
    def glGetAttribLocation(self, program: int, name: str) -> int: ...
    def glGetProgramiv(self, program: int, pname: int) -> typing.Union[int, typing.Tuple[int, int, int]]: ...
    def glGetProgramInfoLog(self, program: int) -> bytes: ...
    def glGetShaderiv(self, shader: int, pname: int) -> int: ...
    def glGetShaderInfoLog(self, shader: int) -> bytes: ...
    def glGetShaderSource(self, shader: int) -> bytes: ...
    def glGetUniformLocation(self, program: int, name: str) -> int: ...
    def glGetVertexAttribdv(self, index: int, pname: int) -> typing.Union[float, typing.Tuple[float, float, float, float]]: ...
    def glGetVertexAttribfv(self, index: int, pname: int) -> typing.Union[float, typing.Tuple[float, float, float, float]]: ...
    def glGetVertexAttribiv(self, index: int, pname: int) -> typing.Union[int, typing.Tuple[int, int, int, int]]: ...
    def glIsProgram(self, program: int) -> int: ...
    def glIsShader(self, shader: int) -> int: ...
    def glLinkProgram(self, program: int) -> None: ...
    def glUseProgram(self, program: int) -> None: ...
    def glUniform1f(self, location: int, v0: float) -> None: ...
    def glUniform2f(self, location: int, v0: float, v1: float) -> None: ...
    def glUniform3f(self, location: int, v0: float, v1: float, v2: float) -> None: ...
    def glUniform4f(self, location: int, v0: float, v1: float, v2: float, v3: float) -> None: ...
    def glUniform1i(self, location: int, v0: int) -> None: ...
    def glUniform2i(self, location: int, v0: int, v1: int) -> None: ...
    def glUniform3i(self, location: int, v0: int, v1: int, v2: int) -> None: ...
    def glUniform4i(self, location: int, v0: int, v1: int, v2: int, v3: int) -> None: ...
    def glUniform1fv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) -> None: ...
    def glUniform2fv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) -> None: ...
    def glUniform3fv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) -> None: ...
    def glUniform4fv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) -> None: ...
    def glUniform1iv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) -> None: ...
    def glUniform2iv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) -> None: ...
    def glUniform3iv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) -> None: ...
    def glUniform4iv(self, location: int, count: int, value: PYQT_OPENGL_ARRAY) -> None: ...
    def glUniformMatrix2fv(self, location: int, count: int, transpose: int, value: PYQT_OPENGL_ARRAY) -> None: ...
    def glUniformMatrix3fv(self, location: int, count: int, transpose: int, value: PYQT_OPENGL_ARRAY) -> None: ...
    def glUniformMatrix4fv(self, location: int, count: int, transpose: int, value: PYQT_OPENGL_ARRAY) -> None: ...
    def glValidateProgram(self, program: int) -> None: ...
    def glVertexAttribPointer(self, index: int, size: int, type: int, normalized: int, stride: int, pointer: PYQT_OPENGL_BOUND_ARRAY) -> None: ...
    def glGenQueries(self, n: int) -> typing.Union[int, typing.Tuple[int, ...]]: ...
    def glDeleteQueries(self, n: int, ids: PYQT_OPENGL_ARRAY) -> None: ...
    def glIsQuery(self, id: int) -> int: ...
    def glBeginQuery(self, target: int, id: int) -> None: ...
    def glEndQuery(self, target: int) -> None: ...
    def glGetQueryiv(self, target: int, pname: int) -> int: ...
    def glBindBuffer(self, target: int, buffer: int) -> None: ...
    def glDeleteBuffers(self, n: int, buffers: PYQT_OPENGL_ARRAY) -> None: ...
    def glGenBuffers(self, n: int) -> typing.Union[int, typing.Tuple[int, ...]]: ...
    def glIsBuffer(self, buffer: int) -> int: ...
    def glBufferData(self, target: int, size: int, data: PYQT_OPENGL_ARRAY, usage: int) -> None: ...
    def glBufferSubData(self, target: int, offset: int, size: int, data: PYQT_OPENGL_ARRAY) -> None: ...
    def glUnmapBuffer(self, target: int) -> int: ...
    def glGetBufferParameteriv(self, target: int, pname: int) -> int: ...
    def glBlendFuncSeparate(self, sfactorRGB: int, dfactorRGB: int, sfactorAlpha: int, dfactorAlpha: int) -> None: ...
    def glPointParameterf(self, pname: int, param: float) -> None: ...
    def glPointParameterfv(self, pname: int, params: PYQT_OPENGL_ARRAY) -> None: ...
    def glPointParameteri(self, pname: int, param: int) -> None: ...
    def glPointParameteriv(self, pname: int, params: PYQT_OPENGL_ARRAY) -> None: ...
    def glActiveTexture(self, texture: int) -> None: ...
    def glSampleCoverage(self, value: float, invert: int) -> None: ...
    def glCompressedTexImage3D(self, target: int, level: int, internalformat: int, width: int, height: int, depth: int, border: int, imageSize: int, data: PYQT_OPENGL_ARRAY) -> None: ...
    def glCompressedTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, imageSize: int, data: PYQT_OPENGL_ARRAY) -> None: ...
    def glCompressedTexImage1D(self, target: int, level: int, internalformat: int, width: int, border: int, imageSize: int, data: PYQT_OPENGL_ARRAY) -> None: ...
    def glCompressedTexSubImage3D(self, target: int, level: int, xoffset: int, yoffset: int, zoffset: int, width: int, height: int, depth: int, format: int, imageSize: int, data: PYQT_OPENGL_ARRAY) -> None: ...
    def glCompressedTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, imageSize: int, data: PYQT_OPENGL_ARRAY) -> None: ...
    def glCompressedTexSubImage1D(self, target: int, level: int, xoffset: int, width: int, format: int, imageSize: int, data: PYQT_OPENGL_ARRAY) -> None: ...
    def glBlendColor(self, red: float, green: float, blue: float, alpha: float) -> None: ...
    def glBlendEquation(self, mode: int) -> None: ...
    def glDrawRangeElements(self, mode: int, start: int, end: int, count: int, type: int, indices: PYQT_OPENGL_ARRAY) -> None: ...
    def glTexImage3D(self, target: int, level: int, internalformat: int, width: int, height: int, depth: int, border: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) -> None: ...
    def glTexSubImage3D(self, target: int, level: int, xoffset: int, yoffset: int, zoffset: int, width: int, height: int, depth: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) -> None: ...
    def glCopyTexSubImage3D(self, target: int, level: int, xoffset: int, yoffset: int, zoffset: int, x: int, y: int, width: int, height: int) -> None: ...
    def glDrawArrays(self, mode: int, first: int, count: int) -> None: ...
    def glDrawElements(self, mode: int, count: int, type: int, indices: PYQT_OPENGL_ARRAY) -> None: ...
    def glPolygonOffset(self, factor: float, units: float) -> None: ...
    def glCopyTexImage1D(self, target: int, level: int, internalformat: int, x: int, y: int, width: int, border: int) -> None: ...
    def glCopyTexImage2D(self, target: int, level: int, internalformat: int, x: int, y: int, width: int, height: int, border: int) -> None: ...
    def glCopyTexSubImage1D(self, target: int, level: int, xoffset: int, x: int, y: int, width: int) -> None: ...
    def glCopyTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, x: int, y: int, width: int, height: int) -> None: ...
    def glTexSubImage1D(self, target: int, level: int, xoffset: int, width: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) -> None: ...
    def glTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) -> None: ...
    def glBindTexture(self, target: int, texture: int) -> None: ...
    def glDeleteTextures(self, n: int, textures: PYQT_OPENGL_ARRAY) -> None: ...
    def glGenTextures(self, n: int) -> typing.Union[int, typing.Tuple[int, ...]]: ...
    def glIsTexture(self, texture: int) -> int: ...
    def glIndexub(self, c: int) -> None: ...
    def glIndexubv(self, c: PYQT_OPENGL_ARRAY) -> None: ...
    def glCullFace(self, mode: int) -> None: ...
    def glFrontFace(self, mode: int) -> None: ...
    def glHint(self, target: int, mode: int) -> None: ...
    def glLineWidth(self, width: float) -> None: ...
    def glPointSize(self, size: float) -> None: ...
    def glPolygonMode(self, face: int, mode: int) -> None: ...
    def glScissor(self, x: int, y: int, width: int, height: int) -> None: ...
    def glTexParameterf(self, target: int, pname: int, param: float) -> None: ...
    def glTexParameterfv(self, target: int, pname: int, params: PYQT_OPENGL_ARRAY) -> None: ...
    def glTexParameteri(self, target: int, pname: int, param: int) -> None: ...
    def glTexParameteriv(self, target: int, pname: int, params: PYQT_OPENGL_ARRAY) -> None: ...
    def glTexImage1D(self, target: int, level: int, internalformat: int, width: int, border: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) -> None: ...
    def glTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, format: int, type: int, pixels: PYQT_OPENGL_ARRAY) -> None: ...
    def glDrawBuffer(self, mode: int) -> None: ...
    def glClear(self, mask: int) -> None: ...
    def glClearColor(self, red: float, green: float, blue: float, alpha: float) -> None: ...
    def glClearStencil(self, s: int) -> None: ...
    def glClearDepth(self, depth: float) -> None: ...
    def glStencilMask(self, mask: int) -> None: ...
    def glColorMask(self, red: int, green: int, blue: int, alpha: int) -> None: ...
    def glDepthMask(self, flag: int) -> None: ...
    def glDisable(self, cap: int) -> None: ...
    def glEnable(self, cap: int) -> None: ...
    def glFinish(self) -> None: ...
    def glFlush(self) -> None: ...
    def glBlendFunc(self, sfactor: int, dfactor: int) -> None: ...
    def glLogicOp(self, opcode: int) -> None: ...
    def glStencilFunc(self, func: int, ref: int, mask: int) -> None: ...
    def glStencilOp(self, fail: int, zfail: int, zpass: int) -> None: ...
    def glDepthFunc(self, func: int) -> None: ...
    def glPixelStoref(self, pname: int, param: float) -> None: ...
    def glPixelStorei(self, pname: int, param: int) -> None: ...
    def glReadBuffer(self, mode: int) -> None: ...
    def glGetBooleanv(self, pname: int) -> typing.Union[bool, typing.Tuple[bool, ...]]: ...
    def glGetDoublev(self, pname: int) -> typing.Union[float, typing.Tuple[float, ...]]: ...
    def glGetError(self) -> int: ...
    def glGetFloatv(self, pname: int) -> typing.Union[float, typing.Tuple[float, ...]]: ...
    def glGetIntegerv(self, pname: int) -> typing.Union[int, typing.Tuple[int, ...]]: ...
    def glGetString(self, name: int) -> str: ...
    def glGetTexParameterfv(self, target: int, pname: int) -> typing.Union[float, typing.Tuple[float, float, float, float]]: ...
    def glGetTexParameteriv(self, target: int, pname: int) -> typing.Union[int, typing.Tuple[int, int, int, int]]: ...
    def glGetTexLevelParameterfv(self, target: int, level: int, pname: int) -> float: ...
    def glGetTexLevelParameteriv(self, target: int, level: int, pname: int) -> int: ...
    def glIsEnabled(self, cap: int) -> int: ...
    def glDepthRange(self, nearVal: float, farVal: float) -> None: ...
    def glViewport(self, x: int, y: int, width: int, height: int) -> None: ...
    def initializeOpenGLFunctions(self) -> bool: ...