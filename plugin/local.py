# -*- coding: utf-8 -*-

from __init__ import _

tstrings = {'mo': _("Mo"),
	'tu': _("Tu"),
	'we': _("We"),
	'th': _("Th"),
	'fr': _("Fr"),
	'sa': _("Sa"),
	'su': _("Su"),
	
	'day_0': _("Sun"),
	'day_1': _("Mon"),
	'day_2': _("Tue"),
	'day_3': _("Wed"),
	'day_4': _("Thu"),
	'day_5': _("Fri"),
	'day_6': _("Sat"),
	
	'monday': _("Monday"),
	'tuesday': _("Tuesday"),
	'wednesday': _("Wednesday"),
	'thursday': _("Thursday"),
	'friday': _("Friday"),
	'saturday': _("Saturday"),
	'sunday': _("Sunday"),
	
	'month_01': _("January"),
	'month_02': _("February"),
	'month_03': _("March"),
	'month_04': _("April"),
	'month_05': _("May"),
	'month_06': _("June"),
	'month_07': _("July"),
	'month_08': _("August"),
	'month_09': _("September"),
	'month_10': _("October"),
	'month_11': _("November"),
	'month_12': _("December"),
	
	'about': _("About"),
	'add_timer': _("Add Timer"),
	'after_event': _("After Event"),
	'agc': _("AGC"),
	'all': _("All"),
	'all_channels': _("All Channels"),
	'authors': _("Authors"),
	'auto': _("Auto"),
	'back': _("Back"),
	'begin': _("Begin"),
	'ber': _("BER"),
	'bouquets': _("Bouquets"),
	'box_info': _("Box Info"),
	'box': _("Box"),
	'boxcontrol': _("Box Control"),
	'box_uptime': _("Box Uptime"),
	'brand': _("Brand"),
	'cancel': _("Cancel"),
	'capacity': _("Capacity"),
	'channel': _("Channel"),
	'channels': _("Channels"),
	'chipset': _("Chipset"),
	'cleanup_timer':_("Cleanup Timers"),
	'contributors': _("Contributors"),
	'control': _("Control"),
	'current': _("Current"),
	'current_event': _("Current Event"),
	'deep_standby': _("Deep-Standby"),
	'default': _("Default"),
	'delete_movie': _("Delete Movie"),
	'delete_movie_question': _("Really delete the movie"),
	'delete_timer': _("Delete Timer"),
	'delete_timer_question': _("Really delete the timer"),
	'description': _("Description"),
	'dhcp': _("DHCP"),
	'disable_timer': _("Disable Timer"),
	'dolby': _("Dolby"),
	'done': _("Done"),
	'download': _("Download"),
	'download_playlist': _("Download Playlist for"),
	'duration': _("Duration"),
	'edit_timer': _("Edit Timer"),
	'enable_timer': _("Enable Timer"),
	'end': _("End"),
	'enabled': _("Enabled"),
	'encrypted': _("Encrypted"),
	'epg': _("EPG"),
	'epgsearch': _("Epg Search"),
	'error': _("Error"),
	'every_timer': _("Every"),
	'extras': _("Extras"),
	'finished': _("finished"),
	'firmware_version': _("Firmware version"),
	'fp_version': _("Frontprocessor Version"),
	'free': _("Free"),
	'free_memory': _("Free Memory"),
	'gateway': _("Gateway"),
	'grabscreenshot': _("Grab Screenshot"),
	'gui_version': _("Gui version"),
	'hidefullremote': _("Hide full remote"),
	'high_resolution': _("High Resolution"),
	'hdd_model': _("Hard disk model"),
	'hour': _("Hour"),
	'ip_address': _("IP address"),
	'ipv6_address': _("IPv6 address(es)"),
	'info': _("Infos"),
	'instant_record': _("Instant Record"),
	'javalib': _("Javascript Libraries"),
	'just_play': _("Just play"),
	'kernel_version': _("Kernel version"),
	'license': _("LICENSE"),
	'loading': _("loading"),
	'location': _("Location"),
	'locked': _("Locked"),
	'mac_address': _("MAC address"),
	'main': _("Main"),
	'minute': _("Minute"),
	'model': _("Model"),
	'movielist': _("Movielist"),
	'movies': _("Movies"),
	'multi_epg': _("MultiEPG"),
	'name': _("Name"),
	'namespace': _("Namespace"),
	'network_interface': _("Network Interface"),
	'no_description_available': _("no description available"),
	'not_implemented': _("Sorry this page is not yet implemented"),
	'nothing': _("Nothing"),
	'nothing_play': _("Nothing playing."),
	'now': _("Now"),
	'on': _("On"),
	'openwebif_header': _("Open Source Web Interface for Linux set-top box"),
	'osd': _("OSD"),
	'playlist': _("Playlist"),
	'powercontrol': _("Power Control"),
	'provider': _("Provider"),
	'providers': _("Providers"),
	'radio': _("Radio"),
	'reboot_box': _("Reboot Box"),
	'rec_status': _("Recording Status"),
	'refresh': _("Refresh"),
	'refresh_auto': _("Refresh automatically every"),
	'remote': _("Remote"),
	'remotecontrol': _("Remote Control"),
	'repeated': _("Repeated"),
	'restart_gui': _("Restart GUI"),
	'running': _("running"),
	'satellites': _("Satellites"),
	'satfinder': _("Satfinder"),
	'save': _("Save"),
	'screenshot': _("Screenshot"),
	'search': _("Search"),
	'search_imdb': _("Search IMDb"),
	'seconds': _("seconds"),
	'send_message': _("Send Message"),
	'sendamessage': _("Send a Message"),
	'service': _("Service"),
	'settings': _("Settings"),
	'shiftforlong': _("(shift + click for long pressure)"),
	'show_full_openwebif': _("Show Full OpenWebif"),
	'showfullremote': _("Show full remote"),
	'show_epg_for': _("Show EPG for"),
	'shutdown': _("Shutdown"),
	'site_source': _("Site and sources"),
	'snr': _("SNR"),
	'software': _("Software"),
	'standby': _("Standby"),
	'standby_toggle': _("Standby Toggle"),
	'start_after_end': _("Start time is after end time"),
	'start_instant_record': _("Start Instant Record"),
	'stream': _("Stream"),
	'subnet_mask': _("Subnet mask"),
	'subservices': _("Subservices"),
	'tags': _("Tags"),
	'teletext': _("Teletext"),
	'television': _("Television"),
	'template_engine': _("Template Engine"),
	'text': _("Text"),
	'time': _("Time"),
	'timeout': _("Timeout"),
	'timer_list': _("Timerlist"),
	'timer': _("Timer"),
	'timers': _("Timers"),
	'title': _("Title"),
	'total_memory': _("Total Memory"),
	'tuner_ber': _("Tuner Bit Error Rate BER"),
	'tuner_number': _("Tuner Number (0-3)"),
	'tuner_signal': _("Tuner Signal"),
	'tuner_signal_snr': _("Tuner Signal Quality SNR"),
	'tuner_signal_snr_db': _("Tuner Signal Quality SNR_DB"),
	'tuner_signal_agc': _("Tuner Signal Power AGC"),
	'tuner_type': _("Tuner Type"),
	'tuners': _("Tuners"),
	'tv': _("TV"),
	'tv_multi_epg': _("TV Multi EPG"),
	'type': _("Type"),
	'upcoming_events': _("Upcoming Events"),
	'version': _("Version"),
	'video': _("Video"),
	'video_height': _("Video Height"),
	'video_wide': _("Video Wide"),
	'video_width': _("Video Width"),
	'volume': _("Volume"),
	'volumecontrol': _("Volume Control"),
	'waiting': _("waiting"),
	'warning': _("Warning"),
	'yes_no': _("Yes/No"),
	'zap': _("Zap"),
	'zapbeforestream': _("zap before Stream"),
	'zap_to': _("Zap to"),
	}
