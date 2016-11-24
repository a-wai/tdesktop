# This file is part of Telegram Desktop,
# the official desktop version of Telegram messaging app, see https://telegram.org
#
# Telegram Desktop is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# It is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# In addition, as a special exception, the copyright holders give permission
# to link the code of portions of this program with the OpenSSL library.
#
# Full license: https://github.com/telegramdesktop/tdesktop/blob/master/LICENSE
# Copyright (c) 2014 John Preston, https://desktop.telegram.org

{
  'includes': [
    'common.gypi',
  ],
  'targets': [{
    'target_name': 'Telegram',
    'variables': {
      'variables': {
        'libs_loc': '../../../Libraries',
      },
      'libs_loc': '<(libs_loc)',
      'src_loc': '../SourceFiles',
      'res_loc': '../Resources',
      'third_party_loc': '../ThirdParty',
      'minizip_loc': '<(third_party_loc)/minizip',
      'sp_media_key_tap_loc': '<(third_party_loc)/SPMediaKeyTap',
      'style_files': [
        '<(res_loc)/colors.palette',
        '<(res_loc)/basic.style',
        '<(res_loc)/basic_types.style',
        '<(src_loc)/boxes/boxes.style',
        '<(src_loc)/dialogs/dialogs.style',
        '<(src_loc)/history/history.style',
        '<(src_loc)/intro/intro.style',
        '<(src_loc)/media/view/mediaview.style',
        '<(src_loc)/media/player/media_player.style',
        '<(src_loc)/overview/overview.style',
        '<(src_loc)/profile/profile.style',
        '<(src_loc)/settings/settings.style',
        '<(src_loc)/stickers/stickers.style',
        '<(src_loc)/ui/widgets/widgets.style',
        '<(src_loc)/window/window.style',
      ],
      'langpacks': [
        'en',
        'de',
        'es',
        'it',
        'nl',
        'ko',
        'pt-BR',
      ],
      'travis_defines%': '',
    },
    'includes': [
      'common_executable.gypi',
      'telegram_qrc.gypi',
      'telegram_win.gypi',
      'telegram_mac.gypi',
      'telegram_linux.gypi',
      'qt.gypi',
      'qt_rcc.gypi',
      'codegen_rules.gypi',
    ],

    'dependencies': [
      'codegen.gyp:codegen_style',
      'codegen.gyp:codegen_numbers',
      'codegen.gyp:MetaLang',
      'utils.gyp:Updater',
    ],

    'defines': [
      'AL_LIBTYPE_STATIC',
      '<!@(python -c "for s in \'<(travis_defines)\'.split(\',\'): print(s)")',
    ],

    'include_dirs': [
      '<(src_loc)',
      '<(SHARED_INTERMEDIATE_DIR)',
      '<(libs_loc)/breakpad/src',
      '<(libs_loc)/lzma/C',
      '<(libs_loc)/libexif-0.6.20',
      '<(libs_loc)/zlib-1.2.8',
      '<(libs_loc)/ffmpeg',
      '<(libs_loc)/openal-soft/include',
      '<(minizip_loc)',
      '<(sp_media_key_tap_loc)',
    ],
    'sources': [
      '<@(qrc_files)',
      '<@(style_files)',
      '<(src_loc)/main.cpp',
      '<(src_loc)/stdafx.cpp',
      '<(src_loc)/stdafx.h',
      '<(src_loc)/apiwrap.cpp',
      '<(src_loc)/apiwrap.h',
      '<(src_loc)/app.cpp',
      '<(src_loc)/app.h',
      '<(src_loc)/application.cpp',
      '<(src_loc)/application.h',
      '<(src_loc)/autoupdater.cpp',
      '<(src_loc)/autoupdater.h',
      '<(src_loc)/config.h',
      '<(src_loc)/dialogswidget.cpp',
      '<(src_loc)/dialogswidget.h',
      '<(src_loc)/facades.cpp',
      '<(src_loc)/facades.h',
      '<(src_loc)/fileuploader.cpp',
      '<(src_loc)/fileuploader.h',
      '<(src_loc)/history.cpp',
      '<(src_loc)/history.h',
      '<(src_loc)/historywidget.cpp',
      '<(src_loc)/historywidget.h',
      '<(src_loc)/lang.cpp',
      '<(src_loc)/lang.h',
      '<(src_loc)/langloaderplain.cpp',
      '<(src_loc)/langloaderplain.h',
      '<(src_loc)/layerwidget.cpp',
      '<(src_loc)/layerwidget.h',
      '<(src_loc)/layout.cpp',
      '<(src_loc)/layout.h',
      '<(src_loc)/mediaview.cpp',
      '<(src_loc)/mediaview.h',
      '<(src_loc)/observer_peer.cpp',
      '<(src_loc)/observer_peer.h',
      '<(src_loc)/overviewwidget.cpp',
      '<(src_loc)/overviewwidget.h',
      '<(src_loc)/passcodewidget.cpp',
      '<(src_loc)/passcodewidget.h',
      '<(src_loc)/localimageloader.cpp',
      '<(src_loc)/localimageloader.h',
      '<(src_loc)/localstorage.cpp',
      '<(src_loc)/localstorage.h',
      '<(src_loc)/logs.cpp',
      '<(src_loc)/logs.h',
      '<(src_loc)/mainwidget.cpp',
      '<(src_loc)/mainwidget.h',
      '<(src_loc)/settings.cpp',
      '<(src_loc)/settings.h',
      '<(src_loc)/shortcuts.cpp',
      '<(src_loc)/shortcuts.h',
      '<(src_loc)/structs.cpp',
      '<(src_loc)/structs.h',
      '<(src_loc)/mainwindow.cpp',
      '<(src_loc)/mainwindow.h',
      '<(src_loc)/boxes/aboutbox.cpp',
      '<(src_loc)/boxes/aboutbox.h',
      '<(src_loc)/boxes/abstractbox.cpp',
      '<(src_loc)/boxes/abstractbox.h',
      '<(src_loc)/boxes/addcontactbox.cpp',
      '<(src_loc)/boxes/addcontactbox.h',
      '<(src_loc)/boxes/autolockbox.cpp',
      '<(src_loc)/boxes/autolockbox.h',
      '<(src_loc)/boxes/backgroundbox.cpp',
      '<(src_loc)/boxes/backgroundbox.h',
      '<(src_loc)/boxes/confirmbox.cpp',
      '<(src_loc)/boxes/confirmbox.h',
      '<(src_loc)/boxes/confirmphonebox.cpp',
      '<(src_loc)/boxes/confirmphonebox.h',
      '<(src_loc)/boxes/connectionbox.cpp',
      '<(src_loc)/boxes/connectionbox.h',
      '<(src_loc)/boxes/contactsbox.cpp',
      '<(src_loc)/boxes/contactsbox.h',
      '<(src_loc)/boxes/downloadpathbox.cpp',
      '<(src_loc)/boxes/downloadpathbox.h',
      '<(src_loc)/boxes/emojibox.cpp',
      '<(src_loc)/boxes/emojibox.h',
      '<(src_loc)/boxes/languagebox.cpp',
      '<(src_loc)/boxes/languagebox.h',
      '<(src_loc)/boxes/localstoragebox.cpp',
      '<(src_loc)/boxes/localstoragebox.h',
      '<(src_loc)/boxes/members_box.cpp',
      '<(src_loc)/boxes/members_box.h',
      '<(src_loc)/boxes/notifications_box.cpp',
      '<(src_loc)/boxes/notifications_box.h',
      '<(src_loc)/boxes/passcodebox.cpp',
      '<(src_loc)/boxes/passcodebox.h',
      '<(src_loc)/boxes/photocropbox.cpp',
      '<(src_loc)/boxes/photocropbox.h',
      '<(src_loc)/boxes/photosendbox.cpp',
      '<(src_loc)/boxes/photosendbox.h',
      '<(src_loc)/boxes/report_box.cpp',
      '<(src_loc)/boxes/report_box.h',
      '<(src_loc)/boxes/sessionsbox.cpp',
      '<(src_loc)/boxes/sessionsbox.h',
      '<(src_loc)/boxes/sharebox.cpp',
      '<(src_loc)/boxes/sharebox.h',
      '<(src_loc)/boxes/stickersetbox.cpp',
      '<(src_loc)/boxes/stickersetbox.h',
      '<(src_loc)/boxes/stickers_box.cpp',
      '<(src_loc)/boxes/stickers_box.h',
      '<(src_loc)/boxes/usernamebox.cpp',
      '<(src_loc)/boxes/usernamebox.h',
      '<(src_loc)/core/build_config.h',
      '<(src_loc)/core/basic_types.h',
      '<(src_loc)/core/click_handler.cpp',
      '<(src_loc)/core/click_handler.h',
      '<(src_loc)/core/click_handler_types.cpp',
      '<(src_loc)/core/click_handler_types.h',
      '<(src_loc)/core/lambda.h',
      '<(src_loc)/core/observer.cpp',
      '<(src_loc)/core/observer.h',
      '<(src_loc)/core/ordered_set.h',
      '<(src_loc)/core/parse_helper.cpp',
      '<(src_loc)/core/parse_helper.h',
      '<(src_loc)/core/qthelp_regex.h',
      '<(src_loc)/core/qthelp_url.cpp',
      '<(src_loc)/core/qthelp_url.h',
      '<(src_loc)/core/runtime_composer.cpp',
      '<(src_loc)/core/runtime_composer.h',
      '<(src_loc)/core/single_timer.cpp',
      '<(src_loc)/core/single_timer.h',
      '<(src_loc)/core/stl_subset.h',
      '<(src_loc)/core/type_traits.h',
      '<(src_loc)/core/utils.cpp',
      '<(src_loc)/core/utils.h',
      '<(src_loc)/core/vector_of_moveable.h',
      '<(src_loc)/core/version.h',
      '<(src_loc)/core/virtual_method.h',
      '<(src_loc)/core/zlib_help.h',
      '<(src_loc)/data/data_abstract_structure.cpp',
      '<(src_loc)/data/data_abstract_structure.h',
      '<(src_loc)/data/data_drafts.cpp',
      '<(src_loc)/data/data_drafts.h',
      '<(src_loc)/dialogs/dialogs_indexed_list.cpp',
      '<(src_loc)/dialogs/dialogs_indexed_list.h',
      '<(src_loc)/dialogs/dialogs_layout.cpp',
      '<(src_loc)/dialogs/dialogs_layout.h',
      '<(src_loc)/dialogs/dialogs_list.cpp',
      '<(src_loc)/dialogs/dialogs_list.h',
      '<(src_loc)/dialogs/dialogs_row.cpp',
      '<(src_loc)/dialogs/dialogs_row.h',
      '<(src_loc)/history/field_autocomplete.cpp',
      '<(src_loc)/history/field_autocomplete.h',
      '<(src_loc)/history/history_drag_area.cpp',
      '<(src_loc)/history/history_drag_area.h',
      '<(src_loc)/history/history_item.cpp',
      '<(src_loc)/history/history_item.h',
      '<(src_loc)/history/history_location_manager.cpp',
      '<(src_loc)/history/history_location_manager.h',
      '<(src_loc)/history/history_media.h',
      '<(src_loc)/history/history_media_types.cpp',
      '<(src_loc)/history/history_media_types.h',
      '<(src_loc)/history/history_message.cpp',
      '<(src_loc)/history/history_message.h',
      '<(src_loc)/history/history_service_layout.cpp',
      '<(src_loc)/history/history_service_layout.h',
      '<(src_loc)/inline_bots/inline_bot_layout_internal.cpp',
      '<(src_loc)/inline_bots/inline_bot_layout_internal.h',
      '<(src_loc)/inline_bots/inline_bot_layout_item.cpp',
      '<(src_loc)/inline_bots/inline_bot_layout_item.h',
      '<(src_loc)/inline_bots/inline_bot_result.cpp',
      '<(src_loc)/inline_bots/inline_bot_result.h',
      '<(src_loc)/inline_bots/inline_bot_send_data.cpp',
      '<(src_loc)/inline_bots/inline_bot_send_data.h',
      '<(src_loc)/intro/introwidget.cpp',
      '<(src_loc)/intro/introwidget.h',
      '<(src_loc)/intro/introcode.cpp',
      '<(src_loc)/intro/introcode.h',
      '<(src_loc)/intro/introphone.cpp',
      '<(src_loc)/intro/introphone.h',
      '<(src_loc)/intro/intropwdcheck.cpp',
      '<(src_loc)/intro/intropwdcheck.h',
      '<(src_loc)/intro/introsignup.cpp',
      '<(src_loc)/intro/introsignup.h',
      '<(src_loc)/intro/introstart.cpp',
      '<(src_loc)/intro/introstart.h',
      '<(src_loc)/media/player/media_player_button.cpp',
      '<(src_loc)/media/player/media_player_button.h',
      '<(src_loc)/media/player/media_player_cover.cpp',
      '<(src_loc)/media/player/media_player_cover.h',
      '<(src_loc)/media/player/media_player_instance.cpp',
      '<(src_loc)/media/player/media_player_instance.h',
      '<(src_loc)/media/player/media_player_list.cpp',
      '<(src_loc)/media/player/media_player_list.h',
      '<(src_loc)/media/player/media_player_panel.cpp',
      '<(src_loc)/media/player/media_player_panel.h',
      '<(src_loc)/media/player/media_player_volume_controller.cpp',
      '<(src_loc)/media/player/media_player_volume_controller.h',
      '<(src_loc)/media/player/media_player_widget.cpp',
      '<(src_loc)/media/player/media_player_widget.h',
      '<(src_loc)/media/view/media_clip_controller.cpp',
      '<(src_loc)/media/view/media_clip_controller.h',
      '<(src_loc)/media/view/media_clip_playback.cpp',
      '<(src_loc)/media/view/media_clip_playback.h',
      '<(src_loc)/media/view/media_clip_volume_controller.cpp',
      '<(src_loc)/media/view/media_clip_volume_controller.h',
      '<(src_loc)/media/media_audio.cpp',
      '<(src_loc)/media/media_audio.h',
      '<(src_loc)/media/media_audio_ffmpeg_loader.cpp',
      '<(src_loc)/media/media_audio_ffmpeg_loader.h',
      '<(src_loc)/media/media_audio_loader.cpp',
      '<(src_loc)/media/media_audio_loader.h',
      '<(src_loc)/media/media_audio_loaders.cpp',
      '<(src_loc)/media/media_audio_loaders.h',
      '<(src_loc)/media/media_child_ffmpeg_loader.cpp',
      '<(src_loc)/media/media_child_ffmpeg_loader.h',
      '<(src_loc)/media/media_clip_ffmpeg.cpp',
      '<(src_loc)/media/media_clip_ffmpeg.h',
      '<(src_loc)/media/media_clip_implementation.cpp',
      '<(src_loc)/media/media_clip_implementation.h',
      '<(src_loc)/media/media_clip_qtgif.cpp',
      '<(src_loc)/media/media_clip_qtgif.h',
      '<(src_loc)/media/media_clip_reader.cpp',
      '<(src_loc)/media/media_clip_reader.h',
      '<(src_loc)/mtproto/facade.cpp',
      '<(src_loc)/mtproto/facade.h',
      '<(src_loc)/mtproto/auth_key.cpp',
      '<(src_loc)/mtproto/auth_key.h',
      '<(src_loc)/mtproto/connection.cpp',
      '<(src_loc)/mtproto/connection.h',
      '<(src_loc)/mtproto/connection_abstract.cpp',
      '<(src_loc)/mtproto/connection_abstract.h',
      '<(src_loc)/mtproto/connection_auto.cpp',
      '<(src_loc)/mtproto/connection_auto.h',
      '<(src_loc)/mtproto/connection_http.cpp',
      '<(src_loc)/mtproto/connection_http.h',
      '<(src_loc)/mtproto/connection_tcp.cpp',
      '<(src_loc)/mtproto/connection_tcp.h',
      '<(src_loc)/mtproto/core_types.cpp',
      '<(src_loc)/mtproto/core_types.h',
      '<(src_loc)/mtproto/dcenter.cpp',
      '<(src_loc)/mtproto/dcenter.h',
      '<(src_loc)/mtproto/file_download.cpp',
      '<(src_loc)/mtproto/file_download.h',
      '<(src_loc)/mtproto/rsa_public_key.cpp',
      '<(src_loc)/mtproto/rsa_public_key.h',
      '<(src_loc)/mtproto/rpc_sender.cpp',
      '<(src_loc)/mtproto/rpc_sender.h',
      '<(src_loc)/mtproto/scheme_auto.cpp',
      '<(src_loc)/mtproto/scheme_auto.h',
      '<(src_loc)/mtproto/session.cpp',
      '<(src_loc)/mtproto/session.h',
      '<(src_loc)/overview/overview_layout.cpp',
      '<(src_loc)/overview/overview_layout.h',
      '<(src_loc)/pspecific.h',
      '<(src_loc)/pspecific_win.cpp',
      '<(src_loc)/pspecific_win.h',
      '<(src_loc)/pspecific_mac.cpp',
      '<(src_loc)/pspecific_mac.h',
      '<(src_loc)/pspecific_mac_p.mm',
      '<(src_loc)/pspecific_mac_p.h',
      '<(src_loc)/pspecific_linux.cpp',
      '<(src_loc)/pspecific_linux.h',
      '<(src_loc)/platform/linux/linux_gdk_helper.cpp',
      '<(src_loc)/platform/linux/linux_gdk_helper.h',
      '<(src_loc)/platform/linux/linux_libnotify.cpp',
      '<(src_loc)/platform/linux/linux_libnotify.h',
      '<(src_loc)/platform/linux/linux_libs.cpp',
      '<(src_loc)/platform/linux/linux_libs.h',
      '<(src_loc)/platform/linux/file_dialog_linux.cpp',
      '<(src_loc)/platform/linux/file_dialog_linux.h',
      '<(src_loc)/platform/linux/main_window_linux.cpp',
      '<(src_loc)/platform/linux/main_window_linux.h',
      '<(src_loc)/platform/linux/notifications_manager_linux.cpp',
      '<(src_loc)/platform/linux/notifications_manager_linux.h',
      '<(src_loc)/platform/mac/mac_utilities.mm',
      '<(src_loc)/platform/mac/mac_utilities.h',
      '<(src_loc)/platform/mac/main_window_mac.mm',
      '<(src_loc)/platform/mac/main_window_mac.h',
      '<(src_loc)/platform/mac/notifications_manager_mac.mm',
      '<(src_loc)/platform/mac/notifications_manager_mac.h',
      '<(src_loc)/platform/mac/window_title_mac.mm',
      '<(src_loc)/platform/mac/window_title_mac.h',
      '<(src_loc)/platform/win/main_window_win.cpp',
      '<(src_loc)/platform/win/main_window_win.h',
      '<(src_loc)/platform/win/notifications_manager_win.cpp',
      '<(src_loc)/platform/win/notifications_manager_win.h',
      '<(src_loc)/platform/win/window_title_win.cpp',
      '<(src_loc)/platform/win/window_title_win.h',
      '<(src_loc)/platform/win/windows_app_user_model_id.cpp',
      '<(src_loc)/platform/win/windows_app_user_model_id.h',
      '<(src_loc)/platform/win/windows_dlls.cpp',
      '<(src_loc)/platform/win/windows_dlls.h',
      '<(src_loc)/platform/win/windows_event_filter.cpp',
      '<(src_loc)/platform/win/windows_event_filter.h',
      '<(src_loc)/platform/platform_file_dialog.h',
      '<(src_loc)/platform/platform_main_window.h',
      '<(src_loc)/platform/platform_notifications_manager.h',
      '<(src_loc)/platform/platform_window_title.h',
      '<(src_loc)/profile/profile_actions_widget.cpp',
      '<(src_loc)/profile/profile_actions_widget.h',
      '<(src_loc)/profile/profile_block_widget.cpp',
      '<(src_loc)/profile/profile_block_widget.h',
      '<(src_loc)/profile/profile_cover_drop_area.cpp',
      '<(src_loc)/profile/profile_cover_drop_area.h',
      '<(src_loc)/profile/profile_cover.cpp',
      '<(src_loc)/profile/profile_cover.h',
      '<(src_loc)/profile/profile_fixed_bar.cpp',
      '<(src_loc)/profile/profile_fixed_bar.h',
      '<(src_loc)/profile/profile_info_widget.cpp',
      '<(src_loc)/profile/profile_info_widget.h',
      '<(src_loc)/profile/profile_inner_widget.cpp',
      '<(src_loc)/profile/profile_inner_widget.h',
      '<(src_loc)/profile/profile_invite_link_widget.cpp',
      '<(src_loc)/profile/profile_invite_link_widget.h',
      '<(src_loc)/profile/profile_members_widget.cpp',
      '<(src_loc)/profile/profile_members_widget.h',
      '<(src_loc)/profile/profile_section_memento.cpp',
      '<(src_loc)/profile/profile_section_memento.h',
      '<(src_loc)/profile/profile_settings_widget.cpp',
      '<(src_loc)/profile/profile_settings_widget.h',
      '<(src_loc)/profile/profile_shared_media_widget.cpp',
      '<(src_loc)/profile/profile_shared_media_widget.h',
      '<(src_loc)/profile/profile_userpic_button.cpp',
      '<(src_loc)/profile/profile_userpic_button.h',
      '<(src_loc)/profile/profile_widget.cpp',
      '<(src_loc)/profile/profile_widget.h',
      '<(src_loc)/serialize/serialize_common.cpp',
      '<(src_loc)/serialize/serialize_common.h',
      '<(src_loc)/serialize/serialize_document.cpp',
      '<(src_loc)/serialize/serialize_document.h',
      '<(src_loc)/settings/settings_advanced_widget.cpp',
      '<(src_loc)/settings/settings_advanced_widget.h',
      '<(src_loc)/settings/settings_background_widget.cpp',
      '<(src_loc)/settings/settings_background_widget.h',
      '<(src_loc)/settings/settings_block_widget.cpp',
      '<(src_loc)/settings/settings_block_widget.h',
      '<(src_loc)/settings/settings_chat_settings_widget.cpp',
      '<(src_loc)/settings/settings_chat_settings_widget.h',
      '<(src_loc)/settings/settings_cover.cpp',
      '<(src_loc)/settings/settings_cover.h',
      '<(src_loc)/settings/settings_fixed_bar.cpp',
      '<(src_loc)/settings/settings_fixed_bar.h',
      '<(src_loc)/settings/settings_general_widget.cpp',
      '<(src_loc)/settings/settings_general_widget.h',
      '<(src_loc)/settings/settings_info_widget.cpp',
      '<(src_loc)/settings/settings_info_widget.h',
      '<(src_loc)/settings/settings_inner_widget.cpp',
      '<(src_loc)/settings/settings_inner_widget.h',
      '<(src_loc)/settings/settings_notifications_widget.cpp',
      '<(src_loc)/settings/settings_notifications_widget.h',
      '<(src_loc)/settings/settings_privacy_widget.cpp',
      '<(src_loc)/settings/settings_privacy_widget.h',
      '<(src_loc)/settings/settings_scale_widget.cpp',
      '<(src_loc)/settings/settings_scale_widget.h',
      '<(src_loc)/settings/settings_widget.cpp',
      '<(src_loc)/settings/settings_widget.h',
      '<(src_loc)/stickers/emoji_pan.cpp',
      '<(src_loc)/stickers/emoji_pan.h',
      '<(src_loc)/stickers/stickers.cpp',
      '<(src_loc)/stickers/stickers.h',
      '<(src_loc)/ui/buttons/history_down_button.cpp',
      '<(src_loc)/ui/buttons/history_down_button.h',
      '<(src_loc)/ui/buttons/peer_avatar_button.cpp',
      '<(src_loc)/ui/buttons/peer_avatar_button.h',
      '<(src_loc)/ui/effects/cross_animation.cpp',
      '<(src_loc)/ui/effects/cross_animation.h',
      '<(src_loc)/ui/effects/panel_animation.cpp',
      '<(src_loc)/ui/effects/panel_animation.h',
      '<(src_loc)/ui/effects/radial_animation.cpp',
      '<(src_loc)/ui/effects/radial_animation.h',
      '<(src_loc)/ui/effects/rect_shadow.cpp',
      '<(src_loc)/ui/effects/rect_shadow.h',
      '<(src_loc)/ui/effects/ripple_animation.cpp',
      '<(src_loc)/ui/effects/ripple_animation.h',
      '<(src_loc)/ui/effects/round_checkbox.cpp',
      '<(src_loc)/ui/effects/round_checkbox.h',
      '<(src_loc)/ui/effects/slide_animation.cpp',
      '<(src_loc)/ui/effects/slide_animation.h',
      '<(src_loc)/ui/effects/widget_fade_wrap.cpp',
      '<(src_loc)/ui/effects/widget_fade_wrap.h',
      '<(src_loc)/ui/effects/widget_slide_wrap.cpp',
      '<(src_loc)/ui/effects/widget_slide_wrap.h',
      '<(src_loc)/ui/style/style_core.cpp',
      '<(src_loc)/ui/style/style_core.h',
      '<(src_loc)/ui/style/style_core_color.cpp',
      '<(src_loc)/ui/style/style_core_color.h',
      '<(src_loc)/ui/style/style_core_font.cpp',
      '<(src_loc)/ui/style/style_core_font.h',
      '<(src_loc)/ui/style/style_core_icon.cpp',
      '<(src_loc)/ui/style/style_core_icon.h',
      '<(src_loc)/ui/style/style_core_types.cpp',
      '<(src_loc)/ui/style/style_core_types.h',
      '<(src_loc)/ui/text/text.cpp',
      '<(src_loc)/ui/text/text.h',
      '<(src_loc)/ui/text/text_block.cpp',
      '<(src_loc)/ui/text/text_block.h',
      '<(src_loc)/ui/text/text_entity.cpp',
      '<(src_loc)/ui/text/text_entity.h',
      '<(src_loc)/ui/toast/toast.cpp',
      '<(src_loc)/ui/toast/toast.h',
      '<(src_loc)/ui/toast/toast_manager.cpp',
      '<(src_loc)/ui/toast/toast_manager.h',
      '<(src_loc)/ui/toast/toast_widget.cpp',
      '<(src_loc)/ui/toast/toast_widget.h',
      '<(src_loc)/ui/widgets/buttons.cpp',
      '<(src_loc)/ui/widgets/buttons.h',
      '<(src_loc)/ui/widgets/checkbox.cpp',
      '<(src_loc)/ui/widgets/checkbox.h',
      '<(src_loc)/ui/widgets/continuous_sliders.cpp',
      '<(src_loc)/ui/widgets/continuous_sliders.h',
      '<(src_loc)/ui/widgets/discrete_sliders.cpp',
      '<(src_loc)/ui/widgets/discrete_sliders.h',
      '<(src_loc)/ui/widgets/dropdown_menu.cpp',
      '<(src_loc)/ui/widgets/dropdown_menu.h',
      '<(src_loc)/ui/widgets/inner_dropdown.cpp',
      '<(src_loc)/ui/widgets/inner_dropdown.h',
      '<(src_loc)/ui/widgets/input_fields.cpp',
      '<(src_loc)/ui/widgets/input_fields.h',
      '<(src_loc)/ui/widgets/labels.cpp',
      '<(src_loc)/ui/widgets/labels.h',
      '<(src_loc)/ui/widgets/menu.cpp',
      '<(src_loc)/ui/widgets/menu.h',
      '<(src_loc)/ui/widgets/multi_select.cpp',
      '<(src_loc)/ui/widgets/multi_select.h',
      '<(src_loc)/ui/widgets/popup_menu.cpp',
      '<(src_loc)/ui/widgets/popup_menu.h',
      '<(src_loc)/ui/widgets/scroll_area.cpp',
      '<(src_loc)/ui/widgets/scroll_area.h',
      '<(src_loc)/ui/widgets/shadow.cpp',
      '<(src_loc)/ui/widgets/shadow.h',
      '<(src_loc)/ui/widgets/tooltip.cpp',
      '<(src_loc)/ui/widgets/tooltip.h',
      '<(src_loc)/ui/abstract_button.cpp',
      '<(src_loc)/ui/abstract_button.h',
      '<(src_loc)/ui/animation.cpp',
      '<(src_loc)/ui/animation.h',
      '<(src_loc)/ui/countryinput.cpp',
      '<(src_loc)/ui/countryinput.h',
      '<(src_loc)/ui/emoji_config.cpp',
      '<(src_loc)/ui/emoji_config.h',
      '<(src_loc)/ui/filedialog.cpp',
      '<(src_loc)/ui/filedialog.h',
      '<(src_loc)/ui/images.cpp',
      '<(src_loc)/ui/images.h',
      '<(src_loc)/ui/twidget.cpp',
      '<(src_loc)/ui/twidget.h',
      '<(src_loc)/window/main_window.cpp',
      '<(src_loc)/window/main_window.h',
      '<(src_loc)/window/notifications_manager.cpp',
      '<(src_loc)/window/notifications_manager.h',
      '<(src_loc)/window/notifications_manager_default.cpp',
      '<(src_loc)/window/notifications_manager_default.h',
      '<(src_loc)/window/notifications_utilities.cpp',
      '<(src_loc)/window/notifications_utilities.h',
      '<(src_loc)/window/player_wrap_widget.cpp',
      '<(src_loc)/window/player_wrap_widget.h',
      '<(src_loc)/window/section_widget.cpp',
      '<(src_loc)/window/section_widget.h',
      '<(src_loc)/window/window_slide_animation.cpp',
      '<(src_loc)/window/window_slide_animation.h',
      '<(src_loc)/window/top_bar_widget.cpp',
      '<(src_loc)/window/top_bar_widget.h',
      '<(src_loc)/window/window_main_menu.cpp',
      '<(src_loc)/window/window_main_menu.h',
      '<(src_loc)/window/window_theme.cpp',
      '<(src_loc)/window/window_theme.h',
      '<(src_loc)/window/window_theme_warning.cpp',
      '<(src_loc)/window/window_theme_warning.h',
      '<(src_loc)/window/window_title.h',

      '<(sp_media_key_tap_loc)/SPMediaKeyTap.m',
      '<(sp_media_key_tap_loc)/SPMediaKeyTap.h',
      '<(sp_media_key_tap_loc)/SPInvocationGrabbing/NSObject+SPInvocationGrabbing.m',
      '<(sp_media_key_tap_loc)/SPInvocationGrabbing/NSObject+SPInvocationGrabbing.h',
    ],
    'conditions': [
      [ '"<(official_build_target)" != ""', {
        'defines': [
          'CUSTOM_API_ID',
        ],
        'dependencies': [
          'utils.gyp:Packer',
        ],
      }],
      [ '"<(build_linux)" != "1"', {
        'sources!': [
          '<(src_loc)/pspecific_linux.cpp',
          '<(src_loc)/pspecific_linux.h',
          '<(src_loc)/platform/linux/linux_gdk_helper.cpp',
          '<(src_loc)/platform/linux/linux_gdk_helper.h',
          '<(src_loc)/platform/linux/linux_libnotify.cpp',
          '<(src_loc)/platform/linux/linux_libnotify.h',
          '<(src_loc)/platform/linux/linux_libs.cpp',
          '<(src_loc)/platform/linux/linux_libs.h',
          '<(src_loc)/platform/linux/file_dialog_linux.cpp',
          '<(src_loc)/platform/linux/file_dialog_linux.h',
          '<(src_loc)/platform/linux/main_window_linux.cpp',
          '<(src_loc)/platform/linux/main_window_linux.h',
          '<(src_loc)/platform/linux/notifications_manager_linux.cpp',
          '<(src_loc)/platform/linux/notifications_manager_linux.h',
        ],
      }],
      [ '"<(build_mac)" != "1"', {
        'sources!': [
          '<(src_loc)/pspecific_mac.cpp',
          '<(src_loc)/pspecific_mac.h',
          '<(src_loc)/pspecific_mac_p.mm',
          '<(src_loc)/pspecific_mac_p.h',
          '<(src_loc)/platform/mac/mac_utilities.mm',
          '<(src_loc)/platform/mac/mac_utilities.h',
          '<(src_loc)/platform/mac/main_window_mac.mm',
          '<(src_loc)/platform/mac/main_window_mac.h',
          '<(src_loc)/platform/mac/notifications_manager_mac.mm',
          '<(src_loc)/platform/mac/notifications_manager_mac.h',
          '<(src_loc)/platform/mac/window_title_mac.mm',
          '<(src_loc)/platform/mac/window_title_mac.h',
          '<(sp_media_key_tap_loc)/SPMediaKeyTap.m',
          '<(sp_media_key_tap_loc)/SPMediaKeyTap.h',
          '<(sp_media_key_tap_loc)/SPInvocationGrabbing/NSObject+SPInvocationGrabbing.m',
          '<(sp_media_key_tap_loc)/SPInvocationGrabbing/NSObject+SPInvocationGrabbing.h',
        ],
      }],
      [ '"<(build_win)" != "1"', {
        'sources': [
          '<(minizip_loc)/crypt.h',
          '<(minizip_loc)/ioapi.c',
          '<(minizip_loc)/ioapi.h',
          '<(minizip_loc)/zip.c',
          '<(minizip_loc)/zip.h',
          '<(minizip_loc)/unzip.c',
          '<(minizip_loc)/unzip.h',
        ],
        'sources!': [
          '<(src_loc)/pspecific_win.cpp',
          '<(src_loc)/pspecific_win.h',
          '<(src_loc)/platform/win/main_window_win.cpp',
          '<(src_loc)/platform/win/main_window_win.h',
          '<(src_loc)/platform/win/notifications_manager_win.cpp',
          '<(src_loc)/platform/win/notifications_manager_win.h',
	  	    '<(src_loc)/platform/win/window_title_win.cpp',
  	  	  '<(src_loc)/platform/win/window_title_win.h',
          '<(src_loc)/platform/win/windows_app_user_model_id.cpp',
          '<(src_loc)/platform/win/windows_app_user_model_id.h',
          '<(src_loc)/platform/win/windows_dlls.cpp',
          '<(src_loc)/platform/win/windows_dlls.h',
          '<(src_loc)/platform/win/windows_event_filter.cpp',
          '<(src_loc)/platform/win/windows_event_filter.h',
        ],
      }],
    ],
  }],
}
