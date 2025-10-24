################################################################################
#
# rawBoson
#
################################################################################
RAW_BOSON_VERSION = 577756c806949a29ae1f7bccc31897bfc251038a
RAW_BOSON_SITE = $(call github,FLIR,rawBoson,$(RAW_BOSON_VERSION))
RAW_BOSON_LICENSE = BOSON-TOOLS-AND-SOFTWARE-DEVELOPMENT-KIT-LICENSE-AGREEMENT
RAW_BOSON_LICENSE_FILES = BOSON_TOOLS_and_SDK_License_Agreement_-_11-1-18.pdf

define RAW_BOSON_BUILD_CMDS
$(INSTALL) -D -m 644 $(RAW_BOSON_PKGDIR)/src/Makefile $(RAW_BOSON_SRCDIR)/Makefile
$(MAKE) $(TARGET_CONFIGURE_OPTS) -C $(@D) LDFLAGS="-lm" rawBoson
endef
define RAW_BOSON_INSTALL_TARGET_CMDS
$(INSTALL) -D -m 0755 $(@D)/rawBoson $(TARGET_DIR)/usr/bin
endef
$(eval $(generic-package))
