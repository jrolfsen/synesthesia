
scope = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>fileTypes</key>
	<array>
%s
	</array>
	<key>name</key>
	<string>%s</string>
	<key>patterns</key>
	<array>
%s
	</array>
	<key>scopeName</key>
	<string>%s.%s</string>
	<key>uuid</key>
	<string>%s</string>
</dict>
</plist>
"""

additional_extension = """		<string>%s</string>
"""

new_file = """{
	"keywords": {
		"hello": "#0CBDE8",
		"world": "dodgerblue"
		$0
	}
}"""

sample_file = """{
	"include": ["lightmarkdown"],
	"extensions": ["txt", "etc"],
	"autocompletion": false,
	"keywords": {
		"hello world": "#ff0000",
		"(color|colour) aliases": "plum",
		"options are supported too": {
			"colour": "plum",
			"background": "blue",
			"bold": true,
			"italics": true,
			"whole-word": true,
			"case-insensitive": true
		}
		$0
	}
}"""

default_colours = """
		<dict>
			<key>settings</key>
			<dict>
				<key>background</key>
				<string>#000000</string>
				<key>caret</key>
				<string>#9F9F9F</string>
				<key>foreground</key>
				<string>#DEDEDE</string>
				<key>invisibles</key>
				<string>#343434</string>
				<key>lineHighlight</key>
				<string>#2A2A2A</string>
				<key>selection</key>
				<string>#424242</string>
			</dict>
		</dict>
"""

theme = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>name</key>
	<string>%s</string>
	<key>author</key>
	<string>Generated by Synesthesia</string>
	<key>settings</key>
	<array>
		%s
		%s
	</array>
	<key>uuid</key>
	<string>%s</string>
</dict>
</plist>
"""


keyword = """
		<dict>
			<key>match</key>
			<string>%s</string>
			<key>name</key>
			<string>%s</string>
		</dict>
"""

theme_element = """
		<dict>
			<key>name</key>
			<string>%s</string>
			<key>scope</key>
			<string>%s</string>
			<key>settings</key>
			<dict>
%s
			</dict>
		</dict>
"""

theme_element_foreground = """
				<key>foreground</key>
				<string>%s</string>
"""

theme_element_fontstyle = """
				<key>fontStyle</key>
				<string>%s</string>
"""

theme_element_background = """
				<key>background</key>
				<string>%s</string>
"""

additional_settings_extension = "\"%s\""

default_settings = """{
	"color_scheme": "Packages/synesthesia/%s.tmTheme",
	"extensions": [%s]
}
"""
