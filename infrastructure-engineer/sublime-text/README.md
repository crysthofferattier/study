# Sublime Text

## 1. - Package Control

### 1 - **Crtl + Shift + P**

### Install
2 - Install Package Control

## Style

### Monokai Pro

##### [monokai.pro](https://www.monokai.pro/)

2 - Package Control: install package
3 - Search for **monokai pro**

### Theme
2 - Search: **Monokai Pro: select theme**
3 - Select the theme

### Settings

1 - Preferences
2 - Settings

```
"font_face": "Fira Code",
"font_size": 13,
"line_padding_bottom": 7,
```
### Color Sublime (Color schema)

2 - Package Control: install package
3 - Search: **Colorsublime** and install
4 - Step one(1) and search for **Colorsublime: install theme**

### Disable Toogle Minimap

2 - Search: **View: Toogle Minimap**

### Files Icons

2 - Search: **A File Icon**

### Remove Packages

2 - Search: **Package Control: Remove Package**
3 - Search for the package

## 2. - Code Formatter

### Install

2 - Search: **Codeformatter**

```
CodeFormatter has support for the following languages:  
  * PHP - By phpfmt
  * JavaScript/JSON - By JSBeautifier
  * HTML - By JSBeautifier
  * CSS - By JSBeautifier
  * SCSS - By Nishutosh Sharma
  * Python - By PythonTidy (only ST2)
  * Visual Basic/VBScript
```

#### PHP

2 - Install codeformatter for php
	* 2 - Search: **phpfmt**

```
"format_on_save" = true
```

3 - Remove in **Settings - User** (Codeformatter)

```
"php55_compat": false, // PHP 5.5 compatible mode
"psr1": false, // Activate PSR1 style
"psr1_naming": false, // Activate PSR1 style - Section 3 and 4.3 - Class and method names case
"psr2": true, // Activate PSR2 style        
```

#### HTML

1 - Change setting (Setting - User)
2 - format_on_save to **true**

```
"codeformatter_html_options":
{
	...
	"format_on_save": true,
	...
}
```

### HTMLBeautify

#### Install
2 - Search: **HTMLBeautify**

#### Usage
2 - search HTMLBeautify