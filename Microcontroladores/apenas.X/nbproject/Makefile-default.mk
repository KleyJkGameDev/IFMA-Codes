#
# Generated Makefile - do not edit!
#
# Edit the Makefile in the project folder instead (../Makefile). Each target
# has a -pre and a -post target defined where you can add customized code.
#
# This makefile implements configuration specific macros and targets.


# Include project Makefile
ifeq "${IGNORE_LOCAL}" "TRUE"
# do not include local makefile. User is passing all local related variables already
else
include Makefile
# Include makefile containing local settings
ifeq "$(wildcard nbproject/Makefile-local-default.mk)" "nbproject/Makefile-local-default.mk"
include nbproject/Makefile-local-default.mk
endif
endif

# Environment
MKDIR=mkdir -p
RM=rm -f 
MV=mv 
CP=cp 

# Macros
CND_CONF=default
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
IMAGE_TYPE=debug
OUTPUT_SUFFIX=elf
DEBUGGABLE_SUFFIX=elf
FINAL_IMAGE=${DISTDIR}/apenas.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}
else
IMAGE_TYPE=production
OUTPUT_SUFFIX=hex
DEBUGGABLE_SUFFIX=elf
FINAL_IMAGE=${DISTDIR}/apenas.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}
endif

ifeq ($(COMPARE_BUILD), true)
COMPARISON_BUILD=-mafrlcsj
else
COMPARISON_BUILD=
endif

# Object Directory
OBJECTDIR=build/${CND_CONF}/${IMAGE_TYPE}

# Distribution Directory
DISTDIR=dist/${CND_CONF}/${IMAGE_TYPE}

# Source Files Quoted if spaced
SOURCEFILES_QUOTED_IF_SPACED=../Scripts/aulinha01.c ../Scripts/q1.c ../Scripts/q2.c ../Scripts/q3.c ../Scripts/q4.c ../Scripts/pratica_03.c

# Object Files Quoted if spaced
OBJECTFILES_QUOTED_IF_SPACED=${OBJECTDIR}/_ext/1910662041/aulinha01.p1 ${OBJECTDIR}/_ext/1910662041/q1.p1 ${OBJECTDIR}/_ext/1910662041/q2.p1 ${OBJECTDIR}/_ext/1910662041/q3.p1 ${OBJECTDIR}/_ext/1910662041/q4.p1 ${OBJECTDIR}/_ext/1910662041/pratica_03.p1
POSSIBLE_DEPFILES=${OBJECTDIR}/_ext/1910662041/aulinha01.p1.d ${OBJECTDIR}/_ext/1910662041/q1.p1.d ${OBJECTDIR}/_ext/1910662041/q2.p1.d ${OBJECTDIR}/_ext/1910662041/q3.p1.d ${OBJECTDIR}/_ext/1910662041/q4.p1.d ${OBJECTDIR}/_ext/1910662041/pratica_03.p1.d

# Object Files
OBJECTFILES=${OBJECTDIR}/_ext/1910662041/aulinha01.p1 ${OBJECTDIR}/_ext/1910662041/q1.p1 ${OBJECTDIR}/_ext/1910662041/q2.p1 ${OBJECTDIR}/_ext/1910662041/q3.p1 ${OBJECTDIR}/_ext/1910662041/q4.p1 ${OBJECTDIR}/_ext/1910662041/pratica_03.p1

# Source Files
SOURCEFILES=../Scripts/aulinha01.c ../Scripts/q1.c ../Scripts/q2.c ../Scripts/q3.c ../Scripts/q4.c ../Scripts/pratica_03.c



CFLAGS=
ASFLAGS=
LDLIBSOPTIONS=

############# Tool locations ##########################################
# If you copy a project from one host to another, the path where the  #
# compiler is installed may be different.                             #
# If you open this project with MPLAB X in the new host, this         #
# makefile will be regenerated and the paths will be corrected.       #
#######################################################################
# fixDeps replaces a bunch of sed/cat/printf statements that slow down the build
FIXDEPS=fixDeps

.build-conf:  ${BUILD_SUBPROJECTS}
ifneq ($(INFORMATION_MESSAGE), )
	@echo $(INFORMATION_MESSAGE)
endif
	${MAKE}  -f nbproject/Makefile-default.mk ${DISTDIR}/apenas.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}

MP_PROCESSOR_OPTION=18F4550
# ------------------------------------------------------------------------------------
# Rules for buildStep: compile
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
${OBJECTDIR}/_ext/1910662041/aulinha01.p1: ../Scripts/aulinha01.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/aulinha01.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/aulinha01.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c  -D__DEBUG=1  -mdebugger=none   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/aulinha01.p1 ../Scripts/aulinha01.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/aulinha01.d ${OBJECTDIR}/_ext/1910662041/aulinha01.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/aulinha01.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
${OBJECTDIR}/_ext/1910662041/q1.p1: ../Scripts/q1.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q1.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q1.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c  -D__DEBUG=1  -mdebugger=none   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/q1.p1 ../Scripts/q1.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/q1.d ${OBJECTDIR}/_ext/1910662041/q1.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/q1.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
${OBJECTDIR}/_ext/1910662041/q2.p1: ../Scripts/q2.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q2.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q2.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c  -D__DEBUG=1  -mdebugger=none   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/q2.p1 ../Scripts/q2.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/q2.d ${OBJECTDIR}/_ext/1910662041/q2.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/q2.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
${OBJECTDIR}/_ext/1910662041/q3.p1: ../Scripts/q3.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q3.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q3.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c  -D__DEBUG=1  -mdebugger=none   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/q3.p1 ../Scripts/q3.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/q3.d ${OBJECTDIR}/_ext/1910662041/q3.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/q3.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
${OBJECTDIR}/_ext/1910662041/q4.p1: ../Scripts/q4.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q4.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q4.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c  -D__DEBUG=1  -mdebugger=none   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/q4.p1 ../Scripts/q4.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/q4.d ${OBJECTDIR}/_ext/1910662041/q4.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/q4.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
${OBJECTDIR}/_ext/1910662041/pratica_03.p1: ../Scripts/pratica_03.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/pratica_03.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/pratica_03.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c  -D__DEBUG=1  -mdebugger=none   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/pratica_03.p1 ../Scripts/pratica_03.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/pratica_03.d ${OBJECTDIR}/_ext/1910662041/pratica_03.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/pratica_03.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
else
${OBJECTDIR}/_ext/1910662041/aulinha01.p1: ../Scripts/aulinha01.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/aulinha01.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/aulinha01.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/aulinha01.p1 ../Scripts/aulinha01.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/aulinha01.d ${OBJECTDIR}/_ext/1910662041/aulinha01.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/aulinha01.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
${OBJECTDIR}/_ext/1910662041/q1.p1: ../Scripts/q1.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q1.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q1.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/q1.p1 ../Scripts/q1.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/q1.d ${OBJECTDIR}/_ext/1910662041/q1.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/q1.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
${OBJECTDIR}/_ext/1910662041/q2.p1: ../Scripts/q2.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q2.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q2.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/q2.p1 ../Scripts/q2.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/q2.d ${OBJECTDIR}/_ext/1910662041/q2.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/q2.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
${OBJECTDIR}/_ext/1910662041/q3.p1: ../Scripts/q3.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q3.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q3.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/q3.p1 ../Scripts/q3.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/q3.d ${OBJECTDIR}/_ext/1910662041/q3.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/q3.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
${OBJECTDIR}/_ext/1910662041/q4.p1: ../Scripts/q4.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q4.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/q4.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/q4.p1 ../Scripts/q4.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/q4.d ${OBJECTDIR}/_ext/1910662041/q4.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/q4.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
${OBJECTDIR}/_ext/1910662041/pratica_03.p1: ../Scripts/pratica_03.c  nbproject/Makefile-${CND_CONF}.mk 
	@${MKDIR} "${OBJECTDIR}/_ext/1910662041" 
	@${RM} ${OBJECTDIR}/_ext/1910662041/pratica_03.p1.d 
	@${RM} ${OBJECTDIR}/_ext/1910662041/pratica_03.p1 
	${MP_CC} $(MP_EXTRA_CC_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -c   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -DXPRJ_default=$(CND_CONF)  -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits $(COMPARISON_BUILD)  -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     -o ${OBJECTDIR}/_ext/1910662041/pratica_03.p1 ../Scripts/pratica_03.c 
	@-${MV} ${OBJECTDIR}/_ext/1910662041/pratica_03.d ${OBJECTDIR}/_ext/1910662041/pratica_03.p1.d 
	@${FIXDEPS} ${OBJECTDIR}/_ext/1910662041/pratica_03.p1.d $(SILENT) -rsi ${MP_CC_DIR}../  
	
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: assemble
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
else
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: assembleWithPreprocess
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
else
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: link
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
${DISTDIR}/apenas.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}: ${OBJECTFILES}  nbproject/Makefile-${CND_CONF}.mk    ../18f4550_g.lkr
	@${MKDIR} ${DISTDIR} 
	${MP_CC} $(MP_EXTRA_LD_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -Wl,-Map=${DISTDIR}/apenas.X.${IMAGE_TYPE}.map  -D__DEBUG=1  -mdebugger=none  -DXPRJ_default=$(CND_CONF)  -Wl,--defsym=__MPLAB_BUILD=1   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto        $(COMPARISON_BUILD) -Wl,--memorysummary,${DISTDIR}/memoryfile.xml -o ${DISTDIR}/apenas.X.${IMAGE_TYPE}.${DEBUGGABLE_SUFFIX}  ${OBJECTFILES_QUOTED_IF_SPACED}     
	@${RM} ${DISTDIR}/apenas.X.${IMAGE_TYPE}.hex 
	
	
else
${DISTDIR}/apenas.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}: ${OBJECTFILES}  nbproject/Makefile-${CND_CONF}.mk   ../18f4550_g.lkr
	@${MKDIR} ${DISTDIR} 
	${MP_CC} $(MP_EXTRA_LD_PRE) -mcpu=$(MP_PROCESSOR_OPTION) -Wl,-Map=${DISTDIR}/apenas.X.${IMAGE_TYPE}.map  -DXPRJ_default=$(CND_CONF)  -Wl,--defsym=__MPLAB_BUILD=1   -mdfp="${DFP_DIR}/xc8"  -fno-short-double -fno-short-float -memi=wordwrite -O0 -fasmfile -maddrqual=ignore -xassembler-with-cpp -mwarn=-3 -Wa,-a -msummary=-psect,-class,+mem,-hex,-file  -ginhx32 -Wl,--data-init -mno-keep-startup -mno-download -mno-default-config-bits -std=c99 -gdwarf-3 -mstack=compiled:auto:auto:auto     $(COMPARISON_BUILD) -Wl,--memorysummary,${DISTDIR}/memoryfile.xml -o ${DISTDIR}/apenas.X.${IMAGE_TYPE}.${DEBUGGABLE_SUFFIX}  ${OBJECTFILES_QUOTED_IF_SPACED}     
	
	
endif


# Subprojects
.build-subprojects:


# Subprojects
.clean-subprojects:

# Clean Targets
.clean-conf: ${CLEAN_SUBPROJECTS}
	${RM} -r ${OBJECTDIR}
	${RM} -r ${DISTDIR}

# Enable dependency checking
.dep.inc: .depcheck-impl

DEPFILES=$(wildcard ${POSSIBLE_DEPFILES})
ifneq (${DEPFILES},)
include ${DEPFILES}
endif
