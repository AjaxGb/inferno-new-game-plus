import sys

if __name__ == '__main__':
	_, in_file, out_file = sys.argv

	# Read template
	with open('template.html') as template:
		template_parts = template.read().split(r'%%')
	
	# Write HTML
	with open(out_file, 'w') as out_file:
		out_file.write(template_parts[0])

		with open(in_file) as in_file:
			# Write title
			title = []
			for line in in_file:
				line = line.strip()
				if line.startswith('@'):
					title.append(
						' '.join(word[::2]
						for word
						in line[1:].split('  ')))
				else:
					break
			out_file.write(' - '.join(title))
			in_file.seek(0)

			out_file.write(template_parts[1])

			for line in in_file:
				line = line.strip()
				if line.startswith('@'):
					print(f'<h1>{line[1:]}</h1>', file=out_file)
				elif line.startswith('!'):
					print(f'<h2>{line[1:]}</h2>', file=out_file)
				elif line.startswith('>'):
					print(f'<h3>{line[1:]}</h3>', file=out_file)
				else:
					if '/' in line:
						verse, line = line.split('/')
						line = f'<aside class="versenum">{verse}</aside>{line}'
					print(f'<div>{line}</div>', file=out_file)
		
		out_file.write(template_parts[2])
